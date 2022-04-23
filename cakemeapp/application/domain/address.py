from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    house_number = db.Column(db.String(10), nullable=True)
    street = db.Column(db.String(30), nullable=True)
    town = db.Column(db.String(20), nullable=True)
    postcode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=True)
    bakeries_address = db.relationship('Bakeries', backref='bakeries_address')

