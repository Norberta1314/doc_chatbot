#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/17
# @Author  : lyytaw
import os


class InitVectorDb:
    def __init__(self, embedding, init_dir):
        self.embedding = embedding
        self.init_dir = init_dir

    def init_vector_map(self, init_meta_path, total_dir, small_embedding_label):
        os.makedirs(total_dir, exist_ok=True)
        new_meta_file = read_json(init_meta_path)



def init_vector_map(init_dir, init_meta_path, total_dir, embeddings, small_embedding_label):
    init_object = InitVectorDb(embeddings, init_dir)
    init_object.init_vector_map(init_meta_path, total_dir, small_embedding_label)
