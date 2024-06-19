import asyncio
import json
import logging

from BCEmbedding.tools.langchain import BCERerank
from langchain_community.embeddings import HuggingFaceEmbeddings
from tqdm.asyncio import tqdm
import pandas as pd

from doc_query.common.config_utils import config_util
from doc_query.common.utils import read_jsonl, save_answers
from doc_query.query_strategy.query_tool import init_query_map, get_query


def main():
    # 初始化 embedding 和 Reranker
    print(config_util.get_common("model_name"))
    embedding = HuggingFaceEmbeddings(
        model_name=config_util.get_common("model_name")
    )
    reranker_args = {"model": config_util.get_common("reranker_name"), "top_n": 6}
    reranker = BCERerank(**reranker_args)
    init_query_map(embedding, reranker)

    # queries = read_jsonl("question.jsonl")
    queries = read_jsonl("/Users/candy/doc_chatbot_1/question.jsonl")

    # 生成答案
    print("Start generating answers...")

    answers = []
    specific_results = pd.DataFrame(columns=["query", "answer", "source_documents"])
    count = 0
    for query in tqdm(queries, total=len(queries)):
        # question = query["query"].strip("，。、？,.?\n ") + "？"
        question = query["query"]
        logging.info(f"问题：{question}")
        result = get_query(question)
        answer = result["result"]
        answers.append(answer)
        specific_results.loc[count] = [question, answer, json.dumps(result['source_documents'])]
        count += 1
        break

    # 处理结果
    save_answers(queries, answers, "submit_result.jsonl")
    specific_results.to_excel("specific_results.xlsx", index=False)


if __name__ == "__main__":
    main()
