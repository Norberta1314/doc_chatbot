#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/18
# @Author  : lyytaw
import os.path
import shutil

import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import dependable_faiss_import

from doc_query.common.utils import get_file_list, get_vector_index_name, get_logger

logger = get_logger()


def merge_faiss(origin, need):
    vector1 = np.array(origin.index.reconstruct_n(0, origin.index.ntotal))
    vector2 = np.array(origin.index.reconstruct_n(0, need.index.ntotal))

    merged_vectors = np.vstack((vector1, vector2))
    faiss = dependable_faiss_import()
    new_index = faiss.IndexFlatL2(merged_vectors.shape[1])

    new_index.add(merged_vectors)
    vector1.index = new_index


def backup_vector_db(vector_db):
    backup_file = vector_db + "_backup"
    shutil.rmtree(backup_file)
    shutil.copytree(vector_db, backup_file)


def merged_vector_db(need_merged_path, origin_db_path, embeddings):
    print(f"merged, need merged path:{need_merged_path}, origin: {origin_db_path}")
    need_merged_db = FAISS.load_local(need_merged_path, embeddings, index_name=get_vector_index_name(),
                                      allow_dangerous_deserialization=True)
    logger.info("there are %s ids need to be merged", str(len(need_merged_db.index_to_docstore_id)))
    if os.path.exists(origin_db_path):
        origin_db = FAISS.load_local(origin_db_path, embeddings, index_name=get_vector_index_name(),
                                     allow_dangerous_deserialization=True
                                     )
        merge_faiss(origin_db_path, need_merged_db)
        # origin_db.merge_from(need_merged_db)
        origin_db.save_local(origin_db_path, get_vector_index_name())
    else:
        shutil.copytree(need_merged_path, origin_db_path)


def merge_vector_db_main(origin_db_path, need_merged_db_path, embeddings):
    backup_vector_db(origin_db_path)

    need_merged_product_list = get_file_list(need_merged_db_path)

    for product in need_merged_product_list:
        product_path = os.path.join(need_merged_db_path, product)

        origin_product_db_path = os.path.join(origin_db_path, product)
        print(f"origin db path {origin_product_db_path}")

        for file_name in get_file_list(product_path):
            need_merged_product = os.path.join(product_path, file_name)

            if os.path.exists(origin_product_db_path):
                merged_vector_db(need_merged_product, origin_product_db_path, embeddings)
            else:
                os.makedirs(origin_product_db_path, exist_ok=True)
                shutil.copytree(need_merged_product, origin_product_db_path)
