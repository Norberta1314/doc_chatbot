import sys
from abc import abstractmethod, ABC

from langchain_community.embeddings import HuggingFaceEmbeddings

from doc_query.common.config_utils import config_util
from doc_query.common.utils import get_path
from doc_query.vector_tool.init_db import init_vector_map
from doc_query.vector_tool.merge import merge_vector_db_main


class VectorBase(ABC):
    @abstractmethod
    def execute(self):
        pass


class VectordbInitStartegy:
    def execute(self):

        init_directory = get_path("doc")
        init_meta_path = get_path("meta.json")
        total_directory = get_path("total_doc")
        init_vector_map(init_directory, init_meta_path, total_directory, embeddings)


class VectordbMergeStartegy:
    def execute(self, origin_db, need_merged_db):
        origin_db = get_path(origin_db)
        need_merge_db = get_path(need_merged_db)
        merge_vector_db_main(origin_db, need_merge_db, embeddings)


if __name__ == '__main__':
    embeddings = HuggingFaceEmbeddings(model_name=config_util.get_common('model_name'), model_kwargs={'device': 'cpu'})

    mode = sys.argv[1]
    if mode == "init":
        VectordbInitStartegy().execute()
    else:
        VectordbMergeStartegy().execute(sys.argv[2], sys.argv[3])
