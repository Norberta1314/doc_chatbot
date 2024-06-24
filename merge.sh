cd doc_query
export PYTHONPATH=/mnt/workspace/doc_chatbot/

rm -rf vectordb/*
python vectordb.py merge total_doc vectordb

rm -rf vector_all_db/*
mkdir vector_all_db/all

cp -r vectordb vector_all_db/all
python vectordb.py merge vector_all_db vectordb

cp -r vectordb doc_chatbot/vectordb