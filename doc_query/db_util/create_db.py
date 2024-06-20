#!/usr/bin/env python
# coding=utf-8

# @Time    : 2024/6/20
# @Author  : lyytaw
from flask_sqlalchemy import SQLALchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERT_KEY'] = "major"
db = SQLALchemy(app)


class VectorTable(db.model):
    __tablename__ = "VECTORTABLE"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)


def create():
    with app.app_context():
        db.create_all()


def add_data(id, title):
    with app.app_context:
        qs = VectorTable(id=id, title=title)
        qs.session.add(qs)
        qs.session.commit()
        return qs.id
