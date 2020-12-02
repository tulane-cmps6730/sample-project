from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
	class Meta:  # Ignoring CSRF security feature.
		csrf = False

	input_field = StringField(label='input headline:', id='input_field',
							  validators=[DataRequired()], 
							  render_kw={'style': 'width:50%'})
	submit = SubmitField('Submit')