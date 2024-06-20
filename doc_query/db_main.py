#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/20
# @Author  : lyytaw
import sys

from doc_query.db_util.create_db import create, init_data

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == "create":
        create()
    else:
        init_data()
