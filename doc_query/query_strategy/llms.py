#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/24
# @Author  : lyytaw
import json

import requests
from langchain_core.language_models import LLM
from zhipuai import ZhipuAI
from doc_query.common.config_utils import config_util


# from llama_index.llms.ollama import Ollama


class ZhipuAILLm:
    def __init__(self):
        self.client = ZhipuAI(api_key=config_util.get_common("GLM_KEY"))

    def query(self, ask_prompt):
        response = self.client.chat.completions.create(
            model="glm-4",  # Fill in the model name to be called
            messages=[
                {"role": "user", "content": ask_prompt}
            ],
        )
        return response.choices[0].message.content


class QianWenLLm:

    def query(self, ask_prompt):
        response = requests.post("http://localhost:11434/api/generate", data=json.dumps({
            "model": "qwen",
            "prompt": ask_prompt,
            "stream": False
        }))
        print(response.json())
        return response.json()["response"]


client = None


def get_llm():
    global client
    if client is not None:
        return client
    if config_util.get_common("llmType") == "zhipu":
        client = ZhipuAILLm()
    else:
        client = QianWenLLm()
    return client
