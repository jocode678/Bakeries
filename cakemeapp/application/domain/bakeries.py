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
    gluten_free_and_coeliac: str
    dairy_free_and_lactose_free: str
    vegetarian: str
    vegan: str
    peanut_free: str
    soy_free: str
    eggs_free: str
    kosher: str
    halal: str
    image: str

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    address_ref = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    opening_times = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    website = db.Column(db.String(50), nullable=True)
    social_media = db.Column(db.String(50), nullable=True)
    gluten_free_and_coeliac= db.Column(db.String(5), nullable=True)
    dairy_free_and_lactose_free= db.Column(db.String(5), nullable=True)
    vegetarian= db.Column(db.String(5), nullable=True)
    vegan= db.Column(db.String(5), nullable=True)
    peanut_free= db.Column(db.String(5), nullable=True)
    soy_free= db.Column(db.String(5), nullable=True)
    eggs_free= db.Column(db.String(5), nullable=True)
    kosher= db.Column(db.String(5), nullable=True)
    halal= db.Column(db.String(5), nullable=True)
    image = db.Column(db.String(), nullable=True)
    customer_member_bakeries = db.relationship('CustomerMember', backref='customer_member_bakeries')
    bakery_owner_bakeries = db.relationship('BakeryOwner', backref='bakery_owner_bakeries')
    reviews_bakeries = db.relationship('Reviews', backref='reviews_bakeries')