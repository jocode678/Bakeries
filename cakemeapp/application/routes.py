from flask import render_template, request, jsonify

from application import app, service
#from application.forms.heroForm import HeroForm
from application.domain.bakeries import Bakeries
from application.domain.address import Address
#from application.domain.dietary import Dietary

@app.route('/')
@app.route('/bakeries', methods=['GET'])
def show_bakeries():
    error = ""
    bakeries = service.get_all_bakeries()
    if len(bakeries) == 0:
        error = "There are no bakeries to display"
    return render_template('bakery.html', bakeries=bakeries, message=error)

# for the sake of example
@app.route('/bakery/<int:bakery_id>', methods=['GET'])
def show_bakery(bakery_id):
    error = ""
    bakery = service.get_bakery_by_id(bakery_id)
    # for the sake of debugging
    # print(bakery.name, bakery.alias)
    if not bakery:
        return jsonify("There are no bakeries with ID: " + str(bakery_id))
    return jsonify(bakery)


@app.route('/teamandheroes/<int:team_id>', methods=['GET'])
def team_and_heroes(team_id):
    error = ""
    team = service.get_team_by_id(team_id)
    if not team:
        error = "There is no team with ID: " + str(team_id)
    return render_template('teams_and_heroes.html', team=team, message=error, title="Team and its Heroes")

@app.route('/new_hero', methods=['GET','POST'])
def add_new_hero():
    error = ""
    form = HeroForm()

    if request.method == 'POST':
        form = HeroForm(request.form)
        print(form.name.data)
        name = form.name.data
        alias = form.alias.data
        superPower = form.superPower.data
        teamID = form.teamID.data


        if len(name) == 0 or len(alias) == 0:
            error = "Please supply both name and alias"
        else:
            hero = Bakeries(name=name, alias=alias, superPower = superPower, teamID = teamID)
            service.add_new_hero(hero)
            heroes = service.get_all_bakeries()
            return render_template('bakery.html', heroes=heroes, message=error)

    return render_template('new_hero_form.html', form=form, message=error)
