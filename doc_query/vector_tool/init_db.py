#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/17
# @Author  : lyytaw
import logging
import os
import re
import shutil

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import MarkdownHeaderTextSplitter, SpacyTextSplitter

from doc_query.common.utils import read_json, get_file_list, obtain_db_path, get_faiss_name

headers_to_split_on = []
for i in range(1, 9):
    headers_to_split_on.append(('#' * i, f"Header {i}"))
markdown_header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
common_text_splitter = SpacyTextSplitter(pipeline="zh_core_web_sm", chunk_size=500, chunk_overlap=100)


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

    def init_vector_db(self, init_dir_path):
        self.splitter()
        index_name = "large.index"
        self.vector = FAISS.from_documents(self.doc_list, self.embeddings)
        self.vector.save_local(get_faiss_name(init_dir_path, self.file_path), index_name)

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
    def __init__(self, embedding, init_dir):
        self.embedding = embedding
        self.init_dir = init_dir

    def init_vector_map(self, init_meta_path, total_dir):
        os.makedirs(total_dir, exist_ok=True)
        new_meta_file = read_json(init_meta_path)
        for meta_info in new_meta_file:
            file_path_name = meta_info["file_name"]
            file_path_list = get_file_list(os.path.join(self.init_dir, file_path_name))
            for file_path in file_path_list:
                if file_path.endswith(".md"):
                    self.init_vector_normal(meta_info, total_dir, file_path)

    def init_vector_normal(self, meta_info, total_dir, file_path):
        cached_sace_path = set()
        product = meta_info["product"]

        init_file_path_origin, _ = obtain_db_path(self.init_dir, product)
        save_path, _ = obtain_db_path(total_dir, product)
        cached_sace_path.add(save_path)

        init_dir_path = self.obtain_init_path(init_file_path_origin, meta_info)
        if not os.listdir(init_dir_path):
            logging.error("Can't init %s", init_dir_path)
        self.init_vector_start(init_dir_path, product, file_path)

    def obtain_init_path(self, init_file_path_origin, meta_info):
        init_file_path, _ = obtain_db_path(self.init_dir, meta_info["product"])
        # if os.path.exists(init_file_path):
        #     shutil.rmtree(init_file_path)
        # shutil.copytree(init_file_path_origin, init_file_path)
        return init_file_path

    def init_vector_start(self, init_dir_path, product, file_name):
        version_base = VersionBase(self.embedding)
        version_base.set_info(product, file_name)
        version_base.add_doc(os.path.join(init_dir_path, file_name))
        version_base.init_vector_db(init_dir_path)


def init_vector_map(init_dir, init_meta_path, total_dir, embeddings):
    init_object = InitVectorDb(embeddings, init_dir)
    init_object.init_vector_map(init_meta_path, total_dir)
