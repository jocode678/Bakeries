from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
@dataclass
class Reviews(db.Model):

    id: int
    review: str
    stars: int
    bakery_ref: int
    image: str

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(300), nullable=True)
    stars = db.Column(db.Integer, nullable=False)
    bakery_ref = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=True)
    image = db.Column(db.String(), nullable=True)


