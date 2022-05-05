from application.domain import bakeries
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


def get_all_addresses():
    return Address.query.all()


def get_bakery(bakery_id):
    bakeries = Bakeries.query.all()
    print(bakeries)
    for bakery in bakeries:
        if bakery.id == bakery_id:
            return bakery
    #for your_bakery in range:
    #if bakery[Bakeries]["id"]== bakery_id:
        #print(["id"], ["shop_name"])
        #return Bakeries["id", "shop_name"]
    #if bakery_id == Bakeries.id:
        #print(Bakeries["id", "shop_name"])
        #ind_bakery= bakery.query.get(bakery_id)
        #ind_bakery = bakeries.query.filter_by(id=bakery.id).first()
        #print(ind_bakery)
        #return ind_bakery


#def get_bakery_by_id(bakery_id):
    #if bakery_id > 0:
        #return Bakeries.query.get(bakery_id)
    #else:
        #return None
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

def get_address_by_id(bakery_id):
    if bakery_id is True:
        return bakeries.query.get(Bakeries.bakery_address)
        #return Address.query.get(bakery_id)
    else:
        return None


def add_new_bakery(bakery):
    db.session.add(bakery)
    db.session.commit()


def add_new_address(address_new):
    db.session.add(address_new)
    db.session.commit()


# This returns the latest added address.
def get_address_id_4():
    var = Address.query.all()
    return str(var[-1].id)



def add_new_review(review):
    db.session.add(review)
    db.session.commit()


# Using this to get the address into the individual bakery page
def get_address_for_bakery(bakery_id):
    if bakery_id > 0:
        address_id = bakery_id
        return Address.query.get(address_id)
    else:
        return None


# CHANGE ABOVE IF TIME - look up address id in the bakery table, don't just assume it will be the same id number

def add_new_customer(customer_member):
    db.session.add(customer_member)
    db.session.commit()


def get_all_reviews():
    return Reviews.query.all()



# Try this for reviews??
# def get_address_by_id(bakery_id):
#     if bakery_id is True:
#         return bakeries.query.get(Bakeries.bakery_address)
#         #return Address.query.get(bakery_id)
#     else:
#         return None


