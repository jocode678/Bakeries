from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application.domain.dietary import Dietary
from application.domain.menu_items import MenuItems
from application.domain.customer_member import CustomerMember
from application.domain.administrator import Administrator
from application.domain.bakery_owner import BakeryOwner
from application.domain.reviews import Reviews
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if sys.platform == 'darwin':
    engine = create_engine('mysql+pymysql://root:@localhost/cakeme', echo=True)
else:
   engine = create_engine('mysql+pymysql://root:password@localhost/cakeme', echo=True)

#engine = create_engine('mysql+pymysql://root:@localhost/cakeme', echo=True)
Session = sessionmaker(bind=engine)


session = Session()

# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()


bakery = session.query(Bakeries).filter_by(id=2).first()
print(bakery.shop_name, bakery.address_ref, bakery.opening_times)

address = session.query(Address).filter_by(id=1).first()
print(address.id, address.house_number, address.postcode)

# Commented out because currently (23.4.22) no data in sql table
# dietary = session.query(Dietary).filter_by(id=1).first()
# print(dietary.id, dietary.category)

# Commented out because currently (23.4.22) no data in sql table
# menu_item = session.query(MenuItems).filter_by(id=1).first()
# print(menu_item.id, menu_item.item_name, menu_item.item_type)

# Commented out because currently (23.4.22) no data in sql table
# customer_member = session.query(CustomerMember).filter_by(id=1).first()
# print(customer_member.id, customer_member.first_name, customer_member.email)

# Commented out because currently (23.4.22) no data in sql table
# administrator = session.query(Administrator).filter_by(id=1).first()
# print(administrator.id, administrator.username, administrator.user_password)

# Commented out because currently (23.4.22) no data in sql table
# bakery_owner = session.query(BakeryOwner).filter_by(id=1).first()
# print(bakery_owner.id, bakery_owner.username, bakery_owner.bakery_ref)

# Commented out because currently (23.4.22) no data in sql table
# review = session.query(Reviews).filter_by(id=1).first()
# print(review.id, review.review, review.stars)


#team = session.query(Address).filter_by(id=4).first()
#print(team.affiliation, team.objective)
#for hero in team.heroes:
    #print(hero.name, '=', hero.alias)
