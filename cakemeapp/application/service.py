from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application.domain.dietary import Dietary
from application.domain.menu_items import MenuItems
from application.domain.customer_member import CustomerMember
from application.domain.administrator import Administrator
from application.domain.bakery_owner import BakeryOwner
from application.domain.reviews import Reviews
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('mysql+pymysql://root:password@localhost/cakeme', echo=True)
# Session = sessionmaker(bind=engine)

from application import db


def get_all_bakeries():
    # alternatively, the db object from application may be used
    # bakeries = db.session.query(Bakeries)
    # return bakeries
    return Bakeries.query.all()


def get_all_dietary_reqs():
    return Dietary.query.with_entities(Dietary.category).all()

# print(get_all_dietary_reqs())


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


def add_new_address(address_new):
    db.session.add(address_new)
    db.session.commit()


# def get_address_id(address_new):
#     return Address.query.all()



# def get_address_id_1(address_new):
#     address = address_new
#     db.session.flush()
#     db.session.refresh(address)
#     return Address.query.get(id)


# print(get_address_id_1('asd'))

# def get_address_id_2():
#     return Address.query.with_entities(Address.id).first()


# print(get_address_id_2())


# def get_address_id_3(address_new):
#     table = Address.query.with_entities(Address.street).all()
#     print('table is', table)
#     print('address_new is', address_new)
#     for row in table:
#         if address_new in Address.street:
#             return Address.id

# print(get_address_id_3('asd'))


def get_address_id_4():
    var = Address.query.all()
    return str(var[-1].id)


def add_new_customer(customer_member):
    db.session.add(customer_member)
    db.session.commit()


