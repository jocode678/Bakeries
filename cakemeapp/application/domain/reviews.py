from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_ref = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    stars = db.Column(db.Integer, nullable=False)
    bakery_ref = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=True)
    image = db.Column(db.String(), nullable=True)


