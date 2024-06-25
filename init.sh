pip install -r requirements.txt
pip install faiss-gpu
pip install langchain==0.1.0
pip install langchain-community==0.0.9
pip install langchain-core==0.1.7
pip install zhipuai
pip install BCEmbedding
pip install transformers==4.32.0
pip install sentence-transformers
pip install rank_bm25
pip install jsonlines
python -m spacy download zh_core_web_sm
cd doc_query
git clone https://www.modelscope.cn/Xorbits/bge-m3.git
git clone https://www.modelscope.cn/maidalun/bce-reranker-base_v1.git