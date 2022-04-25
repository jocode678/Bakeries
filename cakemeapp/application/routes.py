from flask import render_template, request, jsonify

from application import app, service
from application.forms.cakemeForms import BakeryOwnerForm, CustomerSignUpForm
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

# This is working in JSON but not what we want. Jo and Emma 24.4.22
# @app.route('/bakeryjson/<int:bakery_id>', methods=['GET'])
# def show_bakery_json(bakery_id):
#     error = ""
#     bakery = service.get_bakery_by_id(bakery_id)
#     # for the sake of debugging
#     # print(bakery.shop_name, bakery.address_ref)
#     if not bakery:
#         return jsonify("There is no bakery with ID: " + str(bakery_id))
#     return jsonify(bakery)


# This is not working - Jo and Emma 24.4.22
@app.route('/bakery/<int:bakery_id>', methods=['GET'])
def show_bakery(bakery_id):
   error = ""
   bakeries = service.get_bakery_by_id(bakery_id)
   return(bakery_id)
   # if not bakeries:
   #     error = "There is no bakery with ID: " + str(bakery_id)
   # return render_template('individual_bakery.html', bakeries=bakeries, message=error)

# This is not working - Jo and Emma 24.4.22
# @app.route('/myprofile/<int:customer_id>', methods=['GET'])
# def show_customer_profile(customer_id):
#     error = ""
#     customer = service.get_customer_by_id(customer_id)
#     # if len(customer) == 0:
#     #     error = "There is no customer to display"
#     return render_template('my_profile.html', customer=customer, message=error)

# FORMS
@app.route('/new_bakery', methods=['GET','POST'])
def add_new_bakery():
    error = ""
    form = BakeryOwnerForm()

    if request.method == 'POST':
        form = BakeryOwnerForm(request.form)
        print(form.shop_name.data)
        shop_name = form.shop_name.data
        opening_times = form.opening_times.data
        phone = form.phone.data
        website = form.website.data
        social_media = form.social_media.data

        if len(shop_name) == 0 or len(opening_times) == 0 or len(phone) == 0 or len(website) == 0 or len(social_media) == 0:
            error = "Please supply both bakery name and opening times"
        else:
            bakery = Bakeries(shop_name=shop_name, opening_times=opening_times, phone=phone, website=website, social_media=social_media)
            service.add_new_bakery(bakery)
            bakeries = service.get_all_bakeries()
            # change this below to the individual bakery page
            return render_template('bakery.html', bakeries=bakeries, message=error)
    return render_template('new_bakery_form.html', form=form, message=error)

# @app.route('/new_customer_member', methods=['GET', 'POST'])
# def add_new_customer_member():
#     error = ""
#     form = CustomerSignUpForm()
#
#     if request.method == 'POST':
#         form = CustomerSignUpForm(request.form)
#         print(form.username.data)
#         shop_name = form.username.data
#         opening_times = form.user_password.data
#         phone = form.phone.data
#         website = form.website.data
#         social_media = form.social_media.data
#
#         if len(shop_name) == 0 or len(opening_times) == 0 or len(phone) == 0 or len(website) == 0 or len(
#                     social_media) == 0:
#             error = "Please supply both bakery name and opening times"
#         else:
#             bakery = Bakeries(shop_name=shop_name, opening_times=opening_times, phone=phone, website=website,
#                                   social_media=social_media)
#             service.add_new_bakery(bakery)
#             bakeries = service.get_all_bakeries()
#             # change this below to the individual bakery page
#             return render_template('bakery.html', bakeries=bakeries, message=error)
#
#         return render_template('new_bakery_form.html', form=form, message=error)


