from wut4lunch import app
from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField

app.config['SECRET_KEY'] = 'please, tell nobody'

class LunchForm(Form):
    submitter = StringField(u'Hi, my name is')
    food = StringField(u'and I ate')
    # submit button will read "share my lunch!"
    submit = SubmitField(u'share my lunch!')