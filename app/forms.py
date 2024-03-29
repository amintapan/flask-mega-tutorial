from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()]) #many more validators can be used
    remember_me = BooleanField('remember_me', default=False)
