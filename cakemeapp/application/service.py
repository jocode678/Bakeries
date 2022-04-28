from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application.domain.dietary import Dietary
from application.domain.menu_items import MenuItems
from application.domain.customer_member import CustomerMember
from application.domain.administrator import Administrator
from application.domain.bakery_owner import BakeryOwner
from application.domain.reviews import Reviews

from application import db


def get_all_bakeries():
    # alternatively, the db object from application may be used
    # bakeries = db.session.query(Bakeries)
    # return bakeries
    return Bakeries.query.all()


def get_all_dietary_reqs():
    return Dietary.query.with_entities(Dietary.category).all()


def get_bakery_by_id(bakery_id):
    if bakery_id > 0:
        return Bakeries.query.get(bakery_id)
    else:
        return None


def get_customer_by_id(customer_id):
    if customer_id > 0:
        return CustomerMember.query.get(customer_id)
    else:
        return None


# def get_team_by_id(team_id):
#     if team_id < 100:
#         return Address.query.get(team_id)
#     else:
#         return None
#
def add_new_bakery(bakery):
    db.session.add(bakery)
    db.session.commit()


def add_new_customer(customer_member):
    db.session.add(customer_member)
    db.session.commit()


