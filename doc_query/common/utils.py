#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/17
# @Author  : lyytaw
import json
import logging
import os.path
import stat
from typing import Iterable

import jsonlines


def get_url_file_name(path):
    return os.path.join(path, "info.json")


def get_faiss_name(path, product):
    return os.path.abspath(path + os.sep + product + os.sep + "faiss")


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path, content):
    json_content = json.dumps(content)
    modes = stat.S_IWUSR | stat.S_IRUSR

    flags = os.O_WRONLY | os.O_CREAT
    with os.fdopen(os.open(path, flags, modes), "w") as file:
        file.write(json_content)


def comnbine_db_path(ori_db_path, label):
    return os.path.abspath(os.path.join(ori_db_path, label, f"faiss{label}"))


def obtain_db_path(ori_db_path, product):
    dir_path = os.path.abspath(os.path.join(ori_db_path, product))
    return dir_path, os.path.join(dir_path, f"faiss")


def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_logger(name="common"):
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(name + ".log")
    formatter = logging.Formatter('%(asctime)s - (name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def get_source_item(source):
    return f"{source['name']}*******{source['text']}"


def combine_final_source(source, final_source):
    if not final_source:
        return get_source_item(source)
    return f"{final_source}*******{get_source_item(source)}"


def get_file_list(file_path):
    return os.listdir(file_path)


def read_jsonl(path):
    content = []
    with jsonlines.open(path, "r") as json_file:
        for obj in json_file.iter(type=dict, skip_invalid=True):
            content.append(obj)
    return content


def save_answers(
        queries: Iterable, results: Iterable, path: str = "data/answers.jsonl"
):
    answers = []
    for query, result in zip(queries, results):
        answers.append(
            {"id": query["id"], "query": query["query"], "answer": result}
        )

    # use jsonlines to save the answers
    def write_jsonl(path, content):
        with jsonlines.open(path, "w") as json_file:
            json_file.write_all(content)

    # 保存答案到 data/answers.jsonl
    write_jsonl(path, answers)


def get_vector_index_name():
    return "large.index"


def get_source_name(metadata):
    source = metadata.get("source")
    source_file = source[:-3]
    source_file_list = source_file.split(os.sep)

    return source_file_list[-1]
