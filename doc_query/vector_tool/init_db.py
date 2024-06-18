#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/17
# @Author  : lyytaw
import os
import re

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import MarkdownHeaderTextSplitter, SpacyTextSplitter

from doc_query.common.utils import read_json, get_file_list, obtain_db_path, get_faiss_name, get_vector_index_name, \
    get_logger

headers_to_split_on = []
for i in range(1, 9):
    headers_to_split_on.append(('#' * i, f"Header {i}"))
markdown_header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
common_text_splitter = SpacyTextSplitter(pipeline="zh_core_web_sm", chunk_size=500, chunk_overlap=100)

logger = get_logger()

class VersionBase:
    def __init__(self, embedding):
        self.file_name = None
        self.product = None
        self.vector = None
        self.file_path = None
        self.loader = None
        self.doc_list = []
        self.embeddings = embedding

    def add_doc(self, file_path):
        loader = TextLoader(file_path, encoding='utf-8')
        self.loader = loader
        self.file_path = file_path

    def init_vector_db(self, save_path, file_name):
        logger.info("begin splite")
        self.splitter()
        logger.info("end split")
        self.vector = FAISS.from_documents(self.doc_list, self.embeddings)
        logger.info("end from documents")
        self.vector.save_local(get_faiss_name(save_path, file_name[:-3]),
                               get_vector_index_name())

    def splitter(self):
        file_name = os.path.splitext(self.file_path)
        doc_list = self.process_markdown_with_header(file_name, self.loader.file_path)
        for doc in doc_list:
            self.process_page_content(doc)
        self.doc_list.extend(doc_list)

    def process_markdown_with_header(self, file_name, file_path):

        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        md_header_text = markdown_header_splitter.split_text(markdown_text)
        doc_list = []

        for md_content in md_header_text:
            title_mark = ""
            for key, value in md_content.metadata.items():
                if key.startswith("Header"):
                    title_mark += value

            self.process_page_content(md_content)
            split_list = common_text_splitter.split_documents([md_content])
            for split in split_list:
                split.metadata['source'] = file_path
                if title_mark:
                    split.page_content = f"《{file_name}》标题:{title_mark.strip(':')}。内容:{split.page_content}"
            doc_list.extend(split_list)
        return doc_list

    def process_page_content(self, doc):
        doc.page_content = doc.page_content.replace('<br/>', '')
        doc.page_content = re.sub(r"\n\s*\n", "", doc.page_content)
        doc.page_content = re.sub(r"\n{2,}", "", doc.page_content)
        doc.page_content = re.sub(r" {2,}", "", doc.page_content)

    def set_info(self, product, file_name):
        self.product = product
        self.file_name = file_name


class InitVectorDb:
    def __init__(self, embedding, doc_dir):
        self.embedding = embedding
        self.doc_file_dir = doc_dir

    def init_vector_map(self, init_meta_path, total_dir):
        os.makedirs(total_dir, exist_ok=True)
        new_meta_file = read_json(init_meta_path)
        for product_name in new_meta_file:

            file_path_list = get_file_list(os.path.join(self.doc_file_dir, product_name))
            for file_name in file_path_list:
                if file_name.endswith(".md"):
                    self.init_vector_normal(product_name, total_dir, file_name)

    def init_vector_normal(self, product_name, total_dir, file_name):
        logger.info(f"begin init {product_name}, {file_name}")
        save_path, _ = obtain_db_path(total_dir, product_name)
        version_base = VersionBase(self.embedding)
        version_base.set_info(product_name, file_name)
        version_base.add_doc(os.path.join(self.doc_file_dir, product_name, file_name))
        version_base.init_vector_db(save_path, file_name)
        logger.info(f"end init {product_name}, {file_name}")


def init_vector_map(doc_dir, init_meta_path, total_dir, embeddings):
    init_object = InitVectorDb(embeddings, doc_dir)
    init_object.init_vector_map(init_meta_path, total_dir)
