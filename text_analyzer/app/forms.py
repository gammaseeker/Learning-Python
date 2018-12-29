from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    text_input = TextAreaField('Input')#, validators=[DataRequired()])
    delimiter=StringField('Delimiters')
    the_choices = RadioField('Choices', choices = [('countWord','Word Count'), ('countChar','Character Count'), ('freq', 'Most Frequent 5 words')])
    submit=SubmitField('Submit')
