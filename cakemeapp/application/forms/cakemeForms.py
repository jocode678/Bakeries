from flask_wtf import FlaskForm

from application import app, service

from wtforms import StringField, SubmitField, SelectField, IntegerField, validators, Form, BooleanField, PasswordField, TextAreaField, RadioField, FileField
from wtforms.validators import InputRequired, Length


# Form for owners to add their bakery
# making them mandatory?
# how do we solve the foreign-key reference issue with forms?
class BakeryOwnerForm(FlaskForm):
    shop_name = StringField('Bakery Name *')
    house_number = StringField('Street Number')
    street = StringField('Street Name')
    town = StringField('Town')
    postcode = StringField('Postcode')
    country = StringField('Country')
    opening_times = StringField('Opening Times *')
    phone = StringField('Phone Number *')
    website = StringField('Website Link *', [validators.Length(min=1)])
    social_media = StringField("Social Media")
    gluten = RadioField('Gluten Free and Coeliac', choices=[("Yes"), ("No")], default="No")
    dairy_lactose = RadioField('Dairy Free and Lactose Free', choices=[("Yes"), ("No")], default="No")
    vegetarian = RadioField('Vegetarian', choices=[("Yes"), ("No")], default="No")
    vegan = RadioField('Vegan', choices=[("Yes"), ("No")], default="No")
    peanut = RadioField('Peanut Free', choices=[("Yes"), ("No")], default="No")
    soy = RadioField('Soy Free', choices=[("Yes"), ("No")], default="No")
    eggs = RadioField('Eggs Free', choices=[("Yes"), ("No")], default="No")
    fish_shell = RadioField('Fish and Shellfish Free', choices=[("Yes"), ("No")], default="No")
    kosher = RadioField('Kosher', choices=[("Yes"), ("No")], default="No")
    halal = RadioField('Halal', choices=[("Yes"), ("No")], default="No")
    submit = SubmitField('Add Bakery')


class AddReviews(FlaskForm):
    stars = RadioField('Number of stars', choices=[(5), (4), (3), (2), (1)])
    review = StringField('Please tell us more:')
    bakery_ref = StringField('Please enter the bakery ID')
    submit = SubmitField('Add Review')


class UploadImages(FlaskForm):
    image_upload = FileField('Please upload your image')
    bakery_ref = StringField('Please enter the bakery ID')
    submit = SubmitField('Upload image')



class CustomerSignUpForm(FlaskForm):
    username = StringField('Choose a username')
    user_password = StringField('Choose a password')
    # user_password = PasswordField('Choose a password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')])
    # confirm = PasswordField('Confirm your password')
    first_name = StringField('Name')
    last_name = StringField('Surname')
    email = StringField('Email')
    postcode = StringField('Postcode')
    # dietary_ref = -> do a drop-down/options, populated from dietary_ref table
    submit = SubmitField('Sign up')

# form template
# class HeroForm(FlaskForm):
#     name = StringField('Hero Name')
#     alias = StringField('Hero Alias')
#     superPower = StringField('Super Power')
#     teamID = IntegerField('Team ID')
#     submit = SubmitField('Add Hero')
