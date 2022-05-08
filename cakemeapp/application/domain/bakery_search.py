from application import db
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from cakemeapp.application.domain.dietary import Dietary
from flask_msearch import Search
from app import app

db = SQLAlchemy()
search = Search()
search.init_app(app)


# search post
class Post(db.Model):
    __tablename__ = "post"
    __searchable__ = ['shop_name', 'dietary']
