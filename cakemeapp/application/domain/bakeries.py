from application import db
from dataclasses import dataclass
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Bakeries(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    shop_name: str
    address_ref:str
    opening_times: str
    phone: str
    website: str
    social_media: str
    gluten: str
    dairy_lactose: str
    vegetarian: str
    vegan: str
    peanut: str
    soy: str
    eggs: str
    fish_shell: str
    kosher: str
    halal: str
    image: str

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    address_ref = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    address = relationship("Address", back_populates="bakeries", uselist=False)
    opening_times = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    website = db.Column(db.String(50), nullable=True)
    social_media = db.Column(db.String(50), nullable=True)
    gluten= db.Column(db.String(5), nullable=True)
    dairy_lactose= db.Column(db.String(5), nullable=True)
    vegetarian= db.Column(db.String(5), nullable=True)
    vegan= db.Column(db.String(5), nullable=True)
    peanut= db.Column(db.String(5), nullable=True)
    soy= db.Column(db.String(5), nullable=True)
    eggs= db.Column(db.String(5), nullable=True)
    fish_shell = db.Column(db.String(5), nullable=True)
    kosher= db.Column(db.String(5), nullable=True)
    halal= db.Column(db.String(5), nullable=True)
    image = db.Column(db.String(), nullable=True)
    customer_member_bakeries = db.relationship('CustomerMember', backref='customer_member_bakeries')
    bakery_owner_bakeries = db.relationship('BakeryOwner', backref='bakery_owner_bakeries')
    reviews_bakeries = db.relationship('Reviews', backref='reviews_bakeries')