from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application import db


def get_all_bakeries():
    # alternatively, the db object from application may be used
    # bakeries = db.session.query(Bakeries)
    # return bakeries
    return Bakeries.query.all()


def get_bakery_by_id(hero_id):
    if hero_id > 0:
        return Bakeries.query.get(hero_id)
    else:
        return None


def get_team_by_id(team_id):
    if team_id < 100:
        return Address.query.get(team_id)
    else:
        return None


def add_new_hero(hero):
    db.session.add(hero)
    db.session.commit()