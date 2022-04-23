from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application.domain.dietary import Dietary
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

#hero = session.query(Bakeries).filter_by(alias='Iron Man').first()
#print(hero.name, hero.superPower, hero.alias, hero.teamID)

#team = session.query(Address).filter_by(id=4).first()
#print(team.affiliation, team.objective)
#for hero in team.heroes:
    #print(hero.name, '=', hero.alias)
