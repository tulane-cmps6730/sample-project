from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
	class Meta:  # Ignoring CSRF security feature.
		csrf = False

	input_field = StringField(label='input:', id='input_field',
							  validators=[DataRequired()])
	submit = SubmitField('Submit')