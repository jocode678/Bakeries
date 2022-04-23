from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object


class MenuItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(20), nullable=False)
    item_type = db.Column(db.String(20), nullable=True)
    dietary_ref = db.Column(db.Integer, db.ForeignKey('dietary.id'), nullable=True)

