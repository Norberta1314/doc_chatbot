
export PYTHONPATH=/mnt/workspace/doc_chatbot/

rm -rf vectordb/*
mkdir vectordb
cd doc_query
python vectordb.py merge vectordb total_doc
cd ../
rm -rf vector_all_db
mkdir -p vector_all_db

cp -r vectordb vector_all_db/all
cd doc_query
python vectordb.py merge vectordb vector_all_db
cd ../
cp -r vectordb doc_query