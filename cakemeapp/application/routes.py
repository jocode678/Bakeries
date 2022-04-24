from flask import render_template, request, jsonify

from application import app, service
#from application.forms.heroForm import HeroForm
from application.domain.bakeries import Bakeries
from application.domain.address import Address
from application.domain.dietary import Dietary
from application.domain.menu_items import MenuItems
from application.domain.customer_member import CustomerMember
from application.domain.administrator import Administrator
from application.domain.bakery_owner import BakeryOwner
from application.domain.reviews import Reviews

@app.route('/home')
def home_page():
    error = ""
    return render_template('home.html', message=error)

@app.route('/aboutus')
def about_us():
    error = ""
    return render_template('aboutus.html', message=error)


@app.route('/contactus')
def contact_us():
    error = ""
    return render_template('contactus.html', message=error)


@app.route('/bakeries', methods=['GET'])
def show_bakeries():
    error = ""
    bakeries = service.get_all_bakeries()
    if len(bakeries) == 0:
        error = "There are no bakeries to display"
    return render_template('bakery.html', bakeries=bakeries, message=error)


@app.route('/bakeryjson/<int:bakery_id>', methods=['GET'])
def show_bakery_json(bakery_id):
    error = ""
    bakery = service.get_bakery_by_id(bakery_id)
    # for the sake of debugging
    # print(bakery.shop_name, bakery.address_ref)
    if not bakery:
        return jsonify("There is no bakery with ID: " + str(bakery_id))
    return jsonify(bakery)


@app.route('/bakery/<int:bakery_id>', methods=['GET'])
def show_bakery(bakery_id):
    error = ""
    bakeries = service.get_bakery_by_id(bakery_id)
    if not bakeries:
        error = "There is no bakery with ID: " + str(bakery_id)
    return render_template('individual_bakery.html', bakeries=bakeries, message=error)


@app.route('/myprofile/<int:customer_id>', methods=['GET'])
def show_customer_profile(customer_id):
    error = ""
    customer = service.get_customer_by_id(customer_id)
    # if len(customer) == 0:
    #     error = "There is no customer to display"
    return render_template('my_profile.html', customer=customer, message=error)


# @app.route('/new_hero', methods=['GET','POST'])
# def add_new_hero():
#     error = ""
#     form = HeroForm()
#
#     if request.method == 'POST':
#         form = HeroForm(request.form)
#         print(form.name.data)
#         name = form.name.data
#         alias = form.alias.data
#         superPower = form.superPower.data
#         teamID = form.teamID.data
#
#
#         if len(name) == 0 or len(alias) == 0:
#             error = "Please supply both name and alias"
#         else:
#             hero = Bakeries(name=name, alias=alias, superPower = superPower, teamID = teamID)
#             service.add_new_hero(hero)
#             heroes = service.get_all_bakeries()
#             return render_template('bakery.html', heroes=heroes, message=error)
#
#     return render_template('new_hero_form.html', form=form, message=error)
