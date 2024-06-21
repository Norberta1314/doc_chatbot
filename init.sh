pip install -r requirements.txt
pip install langchain==0.1.0
pip install langchain-community==0.0.9
pip install langchain-core==0.1.7
python -m spacy download zh_core_web_sm
pip install faiss-gpu
cp need_change_source_codes/bce_rerank.py /usr/local/lib/python3.10/site-packages/BCEmbedding/tools/langchain/bce_rerank.py
cp need_change_source_codes/faiss.py /usr/local/lib/python3.10/site-packages/langchain_community/vectorstores/faiss.py
cp need_change_source_codes/stuff.py /usr/local/lib/python3.10/site-packages/langchain/chains/combine_documents/stuff.py
cd doc_query
git clone https://www.modelscope.cn/Xorbits/bge-m3.git
git clone https://www.modelscope.cn/maidalun/bce-reranker-base_v1.git
