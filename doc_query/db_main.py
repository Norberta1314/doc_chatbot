import sys

from doc_query.db_util.create_db import create, init_data


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "create":
        create()
    else:
        init_data()