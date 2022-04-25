from application import db
from dataclasses import dataclass


# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Bakeries(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    shop_name: str
    address_ref: int
    opening_times: str
    phone: str
    website: str
    social_media: str
    dietary_ref: int
    image: str

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    address_ref = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    opening_times = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    website = db.Column(db.String(50), nullable=True)
    social_media = db.Column(db.String(50), nullable=True)
    dietary_ref = db.Column(db.Integer, db.ForeignKey('dietary.id'), nullable=True)
    image = db.Column(db.String(), nullable=True)
    customer_member_bakeries = db.relationship('CustomerMember', backref='customer_member_bakeries')
    bakery_owner_bakeries = db.relationship('BakeryOwner', backref='bakery_owner_bakeries')
    reviews_bakeries = db.relationship('Reviews', backref='reviews_bakeries')