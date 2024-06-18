import logging
import os
import re

from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStore
from llama_index.legacy.llms import Ollama

from doc_query.common.config_utils import config_util
from doc_query.common.utils import get_faiss_name, read_json, get_url_file_name

ZH_TEMPLATE = """以下为背景知识：
---------
{context}
---------
请基于给定的背景知识回答问题：```{question}```
如果根据背景知识不能回答或不太确定是否能回答上述问题时，请直接回答：不知道。
"""
SUMMARIZE_TEMPLATE = PromptTemplate(input_variables=["context", "question"], template=ZH_TEMPLATE)
llm = Ollama(model="")

class Qa:
    def __init__(self, db_path, embeddings, reranker, product):
        index_name = "large.index"
        self.embeddings = embeddings
        self.reranker = reranker
        self.url_map = read_json(get_url_file_name(db_path))
        self.vector: VectorStore = FAISS.load_local(get_faiss_name(db_path, product), embeddings, index_name=index_name)
        self.index_to_docstore_id = self.vector.index_to_docstore_id
        self.vector_index_convert = dict(zip(self.vector.index_to_docstore_id, self.vector.index_to_docstore_id.keys()))
        self.retriver = ContextualCompressionRetriever(base_compressor=reranker, base_retriever=self.vector.as_retriever(
            search_type="similarity", search_kwargs={"k": 20, "score_threshold": 0.8}))

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

    def get_source(self, metadata):
        source = metadata.get("source")
        for key in self.url_map:
            if key.lower() in source.lower() or source in key:
                return key
        source = source.split("\\")[-1].split(".")[0]
        return source

    def obtain_contexts_from_vectordb(self, query):
        def obatin_context_anx(doc_id):
            for i in (1, -1):
                new_doc_id = doc_id + i
                if new_doc_id >= 0 and new_doc_id < len(self.index_to_docstore_id):
                    new_content = self.vector.docstore.search(self.index_to_docstore_id[new_doc_id])
                    new_meta = new_content.metadata
                    if self.check_meta(meta_data, new_meta):
                        contexts.add(new_doc_id)

        search_results = self.retriver.get_relevant_documents(query)
        contexts = set()
        for result in search_results:
            meta_data = result[0].metadata
            doc_id = self.vector_index_convert[result[1]]
            obatin_context_anx(doc_id)

        obtained_contexts = {}
        for doc_id in sorted(contexts):
            content = self.vector.docstore.search(self.index_to_docstore_id[doc_id])
            file_name, _ = self.get_source(content.metadata)
            if not obtained_contexts.get(file_name):
                obtained_contexts[file_name] = f"{content.page_content}。\n"
            else:
                obtained_contexts[file_name] = f"{obtained_contexts[file_name]}{content.page_content}。\n"

        contents = self.combine_contexts(obtained_contexts)
        return contents.strip("\n "), search_results

    def first_query(self, query):
        search_results = self.retriver.get_relevant_documents(query)
        if not search_results:
            return "没有找到相关的背景材料", search_results
        context = ""
        for result in search_results:
            file_name, _ = self.get_source(result.metadata)
            context = f"{context}背景材料《{file_name}》：{result.page_content}。\n"
        context = context.strip("\n ")
        result = llm.complete(context)
        return result, search_results

    def second_query(self, query):
        ask_template = f"请用一段话回答问题：{query}"
        result_by_llm = llm.complete(ask_template)
        logging.info(f"llm's answer: {result_by_llm}")
        new_query = f"针对问题：{query}，我们的回答：{result_by_llm}。"
        context, search_results = self.obtain_contexts_from_vectordb(new_query)
        if not context:
            return "没有找到相关的背景材料", search_results
        result = llm.complete(context)
        return result, result_by_llm, search_results

    def third_query(self, query):
        return


    def query(self, query):
        first_result, search_results = self.first_query(query)
        if not search_results or self.check_no_answer(first_result):
            second_result, result_by_llm, search_results = self.second_query(query)
            answer = {"query": query, "result": second_result, "source_documents": search_results}
            if not search_results:
                # 进行第三次检索
                answer["result"] = result_by_llm
            return answer
        return {"query": query, "result": first_result, "source_documents": search_results}


qa_map = {}

def init_qa_map(embeddings, reranker):
    vector_total_path = os.path.abspath(config_util.get_common("vectordb"))
    if not os.path.exists(vector_total_path):
        logging.error("vectordb path is wrong!")
        return
    for product in os.listdir(vector_total_path):
        # product_list = os.path.join(vector_total_path, product)
        qa = Qa(vector_total_path, embeddings, reranker, product)
        qa_map[product] = qa

