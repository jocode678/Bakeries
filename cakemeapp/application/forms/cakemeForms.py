from flask_wtf import FlaskForm

from application import app, service

from wtforms import StringField, SubmitField, IntegerField, validators, Form, BooleanField, PasswordField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Length
# from wtforms import QuerySelectField
# from wtforms import SelectField


# Form for owners to add their bakery
# making them mandatory?
# how do we solve the foreign-key reference issue with forms?
class BakeryOwnerForm(FlaskForm):
    shop_name = StringField('Bakery Name *')
    # address_ref = StringField('Address')
    opening_times = StringField('Opening Times *')
    phone = StringField('Phone Number *')
    website = StringField('Website Link *', [validators.Length(min=1)])
    social_media = StringField("Social Media")
    # dietary_ref = -> do a drop-down/options, populated from dietary_ref table
    dietary_ref = RadioField('Which dietary requirements do you cater for',
                             choices=service.get_all_dietary_reqs()
                             )
    # image =  -> how do you upload?
    submit = SubmitField('Add Bakery')


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
