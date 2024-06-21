from doc_query.common.utils import get_source_name_from_metadata
from doc_query.query_strategy.qa import init_qa_map, qa_map


DEFAULT_PRODUCT = "all"


def init_query_map(embeddings, reranker):
    init_qa_map(embeddings, reranker)


def get_vector(query):
    for vector in qa_map.values():
        find_product = vector.product_match(query)
        if find_product:
            return vector
    return qa_map.get("all")


def get_query(query):
    vector = get_vector(query)
    result = vector.query(query)
    documents = []
    for item in result.get("source_documents", []):
        name = get_source_name_from_metadata(item[0].metadata)
        text = item[0].page_content
        documents.append({"text": text, "name": name, "page": item[0].metadata.get("page")})
    result["result"] = result['result'].replace("<unused1>", "")
    return result

