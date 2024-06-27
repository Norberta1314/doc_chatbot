from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from doc_query.db_util.create_db import VectorTable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vectordb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERT_KEY'] = "major"
db = SQLAlchemy(app)

def search_data_with_meta_info(product, source, title):
    with app.app_context():
        vec_infos = db.session.query(VectorTable).filter((VectorTable.product == product) & (VectorTable.source == source) & (VectorTable.title == title)).order_by(VectorTable.update_time).all()
        return vec_infos


def check_vec_idx_exist(vec_idx):
    with app.app_context():
        qs = db.session.query(VectorTable).filter(VectorTable.vec_idx == vec_idx).all()
        if not qs:
            return False
        return True

def search_data_with_product(product):
    with app.app_context():
        qs = db.session.query(VectorTable).filter(VectorTable.product == product).all()
        return qs