from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Dietary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    bakeries_dietary = db.relationship('Bakeries', backref='bakeries_dietary')