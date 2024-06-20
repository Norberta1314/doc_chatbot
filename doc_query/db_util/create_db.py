#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/20
# @Author  : lyytaw
import os.path

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from doc_query.common.utils import get_file_list, get_source_name

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://vectordb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERT_KEY'] = "major"
db = SQLAlchemy(app)


class VectorTable(db.model):
    __tablename__ = "VECTORTABLE"
    id = db.Column(db.String(256), primary_key=True)
    product = db.Column(db.String(256))
    source = db.Column(db.String(256))
    title = db.Column(db.String(2048))


def create():
    with app.app_context():
        db.create_all()


def add_data(id, product, source, title):
    with app.app_context():
        qs = VectorTable(id=id, product=product, source=source, title=title)
        db.session.add(qs)
        db.session.commit()
        return qs.id


def init_data():
    embeddings = HuggingFaceEmbeddings(model_name="bge-m3", model_kwargs={'device': 'cpu'})
    file_path = "vectordb"
    product_list = get_file_list(file_path)
    for product in product_list:
        faiss_db = FAISS.load_local(os.path.join(product, "faiss"), embeddings,
                                    index_name="large.index")

        for doc_id, vec_index in faiss_db.index_to_docstore_id.items():
            print(doc_id, vec_index)
            content = faiss_db.docstore.search(vec_index)
            source = get_source_name(content.metadata)
            title_mark = ""
            for key, value in content.metadata.items():
                if key.startswith("Header"):
                    title_mark += value
            add_data(vec_index, product, source, title_mark)
