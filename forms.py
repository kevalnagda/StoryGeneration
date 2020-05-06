from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, validators

class ThemeForm(FlaskForm):
	prompt = TextAreaField('prompt', [validators.length(max=500)])
	theme = SelectField('theme', choices=[('Mystery','Mystery'),('Thriller','Thriller'),('Happy','Happy'),('Tragedy','Tragedy'),('Default','Default')])