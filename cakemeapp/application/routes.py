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

# This is working now 25.4.22
@app.route('/bakery/<int:bakery_id>', methods=['GET'])
def show_bakery(bakery_id):
    error = ""
    bakery = service.get_bakery_by_id(bakery_id)
    if not bakery:
        error = "There is no bakery with ID: " + str(bakery_id)
    return render_template('individual_bakery.html', bakery=bakery, message=error)



# This is working now 25.4.22
@app.route('/myprofile/<int:customer_id>', methods=['GET'])
def show_customer_profile(customer_id):
    error = ""
    customer = service.get_customer_by_id(customer_id)
    if not customer:
        error = "There is no customer with ID: " + str(customer_id)
    return render_template('my_profile.html', customer=customer, message=error)


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
        dietary_ref = form.dietary_ref.data

        if len(shop_name) == 0 or len(opening_times) == 0 or len(phone) == 0 or len(website) == 0 or len(social_media) == 0:
            error = "Please fill in all fields with a *"
        else:
            bakery = Bakeries(shop_name=shop_name, opening_times=opening_times, phone=phone, website=website, social_media=social_media, dietary_ref=dietary_ref)
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
#         username = form.username.data
#         user_password = form.user_password.data
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         email = form.email.data
#         postcode = form.postcode.data
#
#         if len(username) == 0 or len(user_password) == 0 or len(first_name) == 0 or len(last_name) == 0 or len(
#                     email) == 0 or len(postcode) == 0:
#             error = "Please supply all information"
#         else:
#             customer_member = CustomerMember(username=username, user_password=user_password, first_name=first_name, last_name=last_name, email=email, postcode=postcode)
#             service.add_new_customer(customer_member)
#             return render_template('aboutus.html', customer_member=customer_member, message=error)
#
#         return render_template('new_customer_form.html', form=form, message=error)


