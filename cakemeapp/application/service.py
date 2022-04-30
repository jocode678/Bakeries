from application.domain import bakeries
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


def get_bakery(bakery_id):
    bakery = Bakeries.query.all()
    print(bakery)
    if bakery_id == Bakeries.id:
        bakery = bakeries.query.filter_by(id=bakery.id).first()
        print(bakery)
        return bakery


#def get_bakery_by_id(bakery_id):
    #if bakery_id > 0:
        #return Bakeries.query.get(bakery_id)
    #else:
        #return None


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

print(get_address_by_id(1))

def add_new_bakery(bakery):
    db.session.add(bakery)
    db.session.commit()
