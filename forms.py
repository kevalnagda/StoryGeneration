from flask_wtf import FlaskForm
from wtforms import RadioField

class ThemeForm(FlaskForm):
	theme = RadioField('Label', choices=[('Mystery','Mystery'),('Thriller','Thriller'),('Happy','Happy'),('Tragedy','Tragedy'),('Default','Default')])