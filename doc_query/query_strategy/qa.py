import logging
import os
import re

from langchain.retrievers import ContextualCompressionRetriever, EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStore
from zhipuai import ZhipuAI

from doc_query.common.config_utils import config_util
from doc_query.common.utils import get_faiss_name, read_json, get_url_file_name, get_file_list, get_path
from doc_query.query_strategy.llms import get_llm
from doc_query.vector_tool.init_db import VersionBase

ZH_TEMPLATE = """上下文信息如下：
---------
{context}
---------
请你基于上下文信息而不是自己的知识，回答问题：```{question}```
回答的要求：1.可以分点作答；2.如果上下文信息中没有相关知识去回答问题，可以回答不确定，不要复述上下文信息。
"""
SUMMARIZE_TEMPLATE = PromptTemplate(input_variables=["context", "question"], template=ZH_TEMPLATE)

client = get_llm()


class Qa:
    def __init__(self, db_path, embeddings, reranker, product):
        index_name = "large.index"
        self.embeddings = embeddings
        self.reranker = reranker
        self.product = product
        self.vector: VectorStore = FAISS.load_local(get_faiss_name(db_path, product), embeddings, index_name=index_name)
        self.index_to_docstore_id = self.vector.index_to_docstore_id
        self.vector_index_convert = dict(zip(self.vector.index_to_docstore_id, self.vector.index_to_docstore_id.keys()))
        self.doc_search = VersionBase(embeddings)
        self.init_doc_list()
        bm25_retriever = BM25Retriever.from_documents(self.doc_search.doc_list)
        bm25_retriever.k = 2
        together_retriever = EnsembleRetriever(retrievers=[bm25_retriever, self.vector.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 30, "score_threshold": 0.8})],
                                               weights=[0.5, 0.5])
        self.retriever = ContextualCompressionRetriever(base_compressor=reranker,
                                                        base_retriever=together_retriever)

    def init_doc_list(self):
        for file in get_file_list(os.path.join(get_path("doc"), self.product)):
            file_path = os.path.join(get_path("doc"), self.product, file)
            self.doc_search.add_doc(file_path)
            self.doc_search.splitter()

    @staticmethod
    def check_no_answer(answer):
        find_no_answer = re.findall("[不无没A][I有法太]?[了确找提清得回语][出到定解楚答认知及言]", answer) if answer else []
        if not answer or find_no_answer:
            return True
        return False

    @staticmethod
    def combine_contexts(texts):
        contents = ""
        for key, value in texts.items():
            contents = f"{contents}背景材料《{key}》：{value}\n"
        return contents

    @staticmethod
    def check_meta(ori_meta, new_meta):
        for key, value in ori_meta.items():
            if not new_meta.get(key) or new_meta.get(key) != value:
                return False
        return True

    def product_match(self, query):
        if self.product in query.lower():
            return True
        return False

    def get_source(self, metadata):
        source = metadata.get("source")
        return source[31:]

    def obtain_contexts_from_vectordb(self, query):
        def obatin_context_anx(doc_id):
            for i in (1, -1):
                new_doc_id = doc_id + i
                if new_doc_id >= 0 and new_doc_id < len(self.index_to_docstore_id):
                    new_content = self.vector.docstore.search(self.index_to_docstore_id[new_doc_id])
                    new_meta = new_content.metadata
                    if self.check_meta(meta_data, new_meta):
                        contexts.add(new_doc_id)

        search_results = self.retriever.get_relevant_documents(query)
        contexts = set()
        for result in search_results:
            meta_data = result[0].metadata
            doc_id = self.vector_index_convert[result[1]]
            obatin_context_anx(doc_id)

        obtained_contexts = {}
        for doc_id in sorted(contexts):
            content = self.vector.docstore.search(self.index_to_docstore_id[doc_id])
            file_name = self.get_source(content.metadata)
            if not obtained_contexts.get(file_name):
                obtained_contexts[file_name] = f"{content.page_content}。\n"
            else:
                obtained_contexts[file_name] = f"{obtained_contexts[file_name]}{content.page_content}。\n"

        contents = self.combine_contexts(obtained_contexts)
        return contents.strip("\n "), search_results

    def first_query(self, query):
        search_results = self.retriever.get_relevant_documents(query)
        if not search_results:
            return "没有找到相关的背景材料", search_results
        context = ""
        for result in search_results:
            file_name = self.get_source(result.metadata)
            context = f"{context}{result.page_content}。\n"
        context = context.strip("\n ")
        # 需要组装template
        ask_prompt = SUMMARIZE_TEMPLATE.format(context=context, question=query)
        # result = llm.acomplete(ask_prompt)
        # return result, search_results
        response = client.query(ask_prompt)
        return response, search_results

    def second_query(self, query):
        ask_template = f"请用一段话回答问题：{query}"
        # result_by_llm = llm.acomplete(ask_template)
        result_by_llm = client.query(ask_template)
        logging.info(f"llm's answer: {result_by_llm}")
        new_query = f"针对问题：{query}，我们的回答：{result_by_llm}。"
        # context, search_results = self.obtain_contexts_from_vectordb(new_query)
        search_results = self.retriever.get_relevant_documents(new_query)
        if not search_results:
            return "没有找到相关的背景材料", result_by_llm, search_results
        context = ""
        for result in search_results:
            file_name = self.get_source(result.metadata)
            context = f"{context}{result.page_content}。\n"
        context = context.strip("\n ")
        # 需要组装template
        ask_prompt = SUMMARIZE_TEMPLATE.format(context=context, question=query)
        # result = llm.acomplete(ask_prompt)
        # return result, result_by_llm, search_results
        response = client.query(ask_prompt)
        return response, result_by_llm, search_results

    def third_query(self, query):
        return

    def query(self, query):
        first_result, search_results = self.first_query(query)
        logging.info(f"first answer: {first_result}")
        if not search_results or self.check_no_answer(first_result):
            second_result, result_by_llm, search_results = self.second_query(query)
            logging.info(f"second answer: {second_result}")
            answer = {"query": query, "result": second_result, "source_documents": search_results}
            # if not search_results:
            #     # 进行第三次检索
            #     logging.info(f"前两次答案为空，所以采用llm自身的答案: {result_by_llm}")
            #     answer["result"] = result_by_llm
            return answer
        return {"query": query, "result": first_result, "source_documents": search_results}


qa_map = {}


def init_qa_map(embeddings, reranker):
    vector_total_path = os.path.abspath(config_util.get_common("vectordb"))
    if not os.path.exists(vector_total_path):
        logging.error("vectordb path is wrong!")
        return
    for product in os.listdir(vector_total_path):
        if product != "director":
            continue
        # product_list = os.path.join(vector_total_path, product)
        qa = Qa(vector_total_path, embeddings, reranker, product)
        qa_map[product] = qa
