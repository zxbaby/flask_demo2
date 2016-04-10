from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import Required, InputRequired, DataRequired, IPAddress


class SnschedulerForm(Form):
    ip = StringField('ip', validators=[IPAddress])
    name = StringField('name', validators=[Required])
    sec = IntegerField('sec')
    min = IntegerField('min')
    hour = IntegerField('hour')
    day = IntegerField('day')
    month = IntegerField('month')
    weekend = IntegerField('weekend')
    start_date = DateTimeField('start_date')
    end_date = DateTimeField('end_date')
    cmd = StringField('cmd',validators=[Required])
    trigger = StringField('trigger', validators=[Required])
    comment = StringField('comment')