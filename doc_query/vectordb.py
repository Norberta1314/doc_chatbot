from abc import abstractmethod, ABC

from doc_query.vector_tool.init_db import init_vector_map


class VectorBase(ABC):
    @abstractmethod
    def execute(self):
        pass


class VectordbInitStartegy:
    def execute(self):
        init_directory = "/Users/lyy/apos/parse/doc"
        init_meta_path = "/Users/lyy/apos/parse/meta.json"
        total_directory = "/Users/lyy/apos/parse/doc_total"
        init_vector_map(init_directory, init_meta_path, total_directory, embeddings)


if __name__ == '__main__':
    # embeddings = HuggingFaceEmbeddings()
    embeddings = ""
    VectordbInitStartegy().execute()
