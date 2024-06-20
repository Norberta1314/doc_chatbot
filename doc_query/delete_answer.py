#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/20
# @Author  : lyytaw
from doc_query.common.utils import read_jsonl
import jsonlines

def write_jsonl(path, content):
    with jsonlines.open(path, "w") as json_file:
        json_file.write_all(content)

if __name__ == '__main__':
    answer_obj = read_jsonl('/Users/lyy/apos/parse/doc_query/submit_result.jsonl')
    for answer in answer_obj:
        answer['answer'] = answer['answer'].replace('\n', '')
    write_jsonl('bb.jsonl')