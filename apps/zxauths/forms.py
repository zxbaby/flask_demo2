from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import Required, InputRequired, DataRequired, IPAddress

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired])
    password = PasswordField('password', validators=[DataRequired])
    submit = SubmitField()



