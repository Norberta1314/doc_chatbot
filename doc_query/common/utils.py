#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/17
# @Author  : lyytaw
import json
import logging
import os.path
import stat


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
