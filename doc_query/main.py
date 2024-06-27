import logging
import time

from BCEmbedding.tools.langchain import BCERerank
from langchain_community.embeddings import HuggingFaceEmbeddings

import pandas as pd

from doc_query.common.config_utils import config_util
from doc_query.common.utils import read_jsonl, write_jsonl
from doc_query.query_strategy.query_tool import init_query_map, get_query


def main():
    # 初始化 embedding 和 Reranker
    print(config_util.get_common("model_name"))
    embedding = HuggingFaceEmbeddings(
        model_name=config_util.get_common("model_name")
    )
    reranker_args = {"model": config_util.get_common("reranker_name"), "top_n": 10}
    reranker = BCERerank(**reranker_args)
    init_query_map(embedding, reranker)

    # queries = read_jsonl("question.jsonl")
    queries = read_jsonl("question.jsonl")

    # 生成答案
    print("Start generating answers...")

    answers = []
    answers_list = []
    specific_results = pd.DataFrame(columns=["query", "answer", "source_documents"])
    count = 0
    for index, query in enumerate(queries):
        print(f"index: {index}")
        # question = query["query"].strip("，。、？,.?\n ") + "？"
        question = query["query"]
        logging.info(f"问题：{question}")
        is_get_result = False
        result = None
        while not is_get_result:
            try:
                result = get_query(question)
                is_get_result = True
            except Exception as e:
                print("error query")
                time.sleep(5)

        answer = result["result"]
        answers.append(answer)
        answers_list.append({
            "id": query["id"],
            "query": question,
            "answer": answer
        })
        specific_results.loc[count] = [question, answer, str(result['source_documents'])]
        count += 1

        # 处理结果
        write_jsonl(answers_list, "result.jsonl")
        specific_results.to_excel("specific_results.xlsx", index=False)


if __name__ == "__main__":
    main()
