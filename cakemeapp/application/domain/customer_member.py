from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class CustomerMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    postcode = db.Column(db.String(10), nullable=True)
    dietary_ref = db.Column(db.Integer, db.ForeignKey('dietary.id'), nullable=True)
    favourite_ref = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=True)

