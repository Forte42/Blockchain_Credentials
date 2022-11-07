from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Class for form 
class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    wallet = StringField('wallet', id="walletInput", validators=[DataRequired()])
    submit = SubmitField()
