pip install -r requirements.txt
python -m spacy download zh_core_web_sm
pip install faiss-gpu
cd doc_query
git clone https://www.modelscope.cn/Xorbits/bge-m3.git
git clone https://www.modelscope.cn/maidalun/bce-reranker-base_v1.git