from flask_wtf import FlaskForm
from wtforms import Form, StringField,PasswordField,validators #biao dan
from wtforms.fields.html5 import EmailField
from user.models import User

class RegistrationForm(FlaskForm):
    name = StringField('Your name' , [validators.DataRequired(), validators.Length(min=2,max=30)])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField ('New Password', [ validators.DataRequired(),
                                                validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')