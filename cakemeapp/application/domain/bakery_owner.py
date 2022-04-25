from application import db


# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object

class BakeryOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    bakery_ref = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=True)

