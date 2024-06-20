import logging
import os
import re

from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStore
from zhipuai import ZhipuAI

from doc_query.common.config_utils import config_util
from doc_query.common.utils import get_faiss_name

ZH_TEMPLATE = """上下文信息如下：
---------
{context}
---------
请你基于上下文信息而不是自己的知识，回答问题：```{question}```
回答的要求：1.可以分点作答；2.如果上下文信息中没有相关知识去回答问题，请直接回答不知道，不要复述上下文信息。
"""
SUMMARIZE_TEMPLATE = PromptTemplate(input_variables=["context", "question"], template=ZH_TEMPLATE)

client = ZhipuAI(api_key=config_util.get_common("GLM_KEY"))


class Qa:
    def __init__(self, db_path, embeddings, reranker, product):
        index_name = "large.index"
        self.embeddings = embeddings
        self.reranker = reranker
        self.product = product
        self.vector: VectorStore = FAISS.load_local(get_faiss_name(db_path, product), embeddings, index_name=index_name)
        self.index_to_docstore_id = self.vector.index_to_docstore_id
        self.vector_index_convert = dict(zip(self.vector.index_to_docstore_id.values(), self.vector.index_to_docstore_id.keys()))
        self.retriever = ContextualCompressionRetriever(base_compressor=reranker,
                                                        base_retriever=self.vector.as_retriever(
                                                            search_type="similarity",
                                                            search_kwargs={"k": 20, "score_threshold": 0.8}))

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

    def get_title(self, metadata):
        title_mark = ""
        for key,value in metadata.items():
            if key == "Header 1":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 2":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 3":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 4":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 5":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 6":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 7":
                title_mark = f"{title_mark}{value}"
            elif key == "Header 8":
                title_mark = f"{title_mark}{value}"
        return title_mark

    def obtain_contexts_from_vectordb(self, query):
        def obatin_context_anx(doc_id):
            for i in (1, -1):
                new_doc_id = doc_id + i
                if new_doc_id >= 0 and new_doc_id < len(self.index_to_docstore_id):
                    new_content = self.vector.docstore.search(self.index_to_docstore_id[new_doc_id])
                    new_meta = new_content[0].metadata
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
            file_name = self.get_source(content[0].metadata)
            if not obtained_contexts.get(file_name):
                obtained_contexts[file_name] = f"{content[0].page_content}。\n"
            else:
                obtained_contexts[file_name] = f"{obtained_contexts[file_name]}{content[0].page_content}。\n"

        contents = self.combine_contexts(obtained_contexts)
        return contents.strip("\n "), search_results

    def first_query(self, query):
        search_results = self.retriever.get_relevant_documents(query)
        if not search_results:
            return "没有找到相关的背景材料", search_results

        context = self.combine_source_documents(search_results)
        # 需要组装template
        ask_prompt = SUMMARIZE_TEMPLATE.format(context=context, question=query)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_prompt}
            ],
        )
        return response.choices[0].message.content, search_results

    def combine_source_documents(self, search_results):
        context_idx_dict = {}
        for result in search_results:
            file_name = self.get_source(result[0].metadata)
            title_value = self.get_title(result[0].metadata)
            file_title = f"材料《{file_name}》{title_value}"
            if context_idx_dict.get(file_title):
                context_idx_dict[file_title].add(self.vector_index_convert[result[1]])
            else:
                context_idx_dict[file_title] = {self.vector_index_convert[result[1]]}

        context = ""
        for title, content_idx in context_idx_dict.items():
            context = f"{title}\n"
            for i, doc_id in enumerate(sorted(content_idx)):
                content = self.vector.docstore.search(self.index_to_docstore_id[doc_id]).page_content
                context = f"{context}片段{i+1}：{content}。\n"

        context = re.sub("[，。 ；：,.:;]+。", "。", context)
        context = context.strip("\n ")
        return context

    def second_query(self, query):
        ask_template = f"请用一段话回答问题：{query}"
        # result_by_llm = llm.acomplete(ask_template)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_template}
            ],
        )
        result_by_llm = response.choices[0].message.content
        logging.info(f"llm's answer: {result_by_llm}")
        new_query = f"针对问题：{query}，我们的回答：{result_by_llm}。"
        # context, search_results = self.obtain_contexts_from_vectordb(new_query)
        search_results = self.retriever.get_relevant_documents(new_query)
        if not search_results:
            return "没有找到相关的背景材料", search_results
        context = self.combine_source_documents(search_results)
        # 需要组装template
        ask_prompt = SUMMARIZE_TEMPLATE.format(context=context, question=query)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_prompt}
            ],
        )
        return response.choices[0].message.content, result_by_llm, search_results

    def third_query(self, query, search_results_by_llm):
        ask_template = f"请回答问题：{query}"
        # result_by_llm = llm.acomplete(ask_template)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_template}
            ],
        )
        result_by_llm = response.choices[0].message.content

        rewrite_prompt = """以下为背景知识：
---------
{context}
---------
请结合背景知识并按照改写的要求，改写下列问题：
---------
{question}
---------
改写的要求：改写后的问题能够更好地从知识库中检索到相关内容。
回答的要求：请直接返回你改写后的问题，不要复述原问题和上下文信息。
        """
        rewrite_template = PromptTemplate(input_variables=["context", "question"], template=rewrite_prompt)
        rewrite_template = rewrite_template.format(question=query, context=result_by_llm)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": rewrite_template}
            ],
        )
        new_question = response.choices[0].message.content
        logging.info(f"改写后的问题: {new_question}")
        search_results_by_rewrite = self.retriever.get_relevant_documents(new_question)
        if not search_results_by_llm and not search_results_by_rewrite:
            return "没有找到相关的背景材料", result_by_llm, search_results_by_rewrite

        search_results_ids = set()
        for result in search_results_by_llm:
            search_results_ids.add(result[1])
        for result in search_results_by_rewrite:
            search_results_ids.add(result[1])

        search_results = []
        for vec_indx in search_results_ids:
            search_results.append((self.vector.docstore.search(vec_indx), vec_indx))
        # 这需要个重排机制
        if len(search_results_ids) > 6:
            search_results = self.reranker.compress_documents(search_results, query)

        context = self.combine_source_documents(search_results)
        # 需要组装template
        ask_prompt = SUMMARIZE_TEMPLATE.format(context=context, question=query)
        response = client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_prompt}
            ],
        )
        return response.choices[0].message.content, result_by_llm, search_results

    def query(self, query):
        first_result, search_results = self.first_query(query)
        logging.info(f"first answer: {first_result}")
        if not search_results or self.check_no_answer(first_result):
            second_result, result_by_llm, search_results = self.second_query(query)
            logging.info(f"second answer: {second_result}")
            answer = {"query": query, "result": second_result, "source_documents": search_results}
            if not search_results or self.check_no_answer(second_result):
                # 进行第三次检索
                third_result, result_by_llm, search_results = self.third_query(query, search_results)
                answer['result'] = third_result
                if not search_results:
                    logging.info(f"前两次答案为空，所以采用llm自身的答案: {result_by_llm}")
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
