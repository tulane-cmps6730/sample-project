from flask import render_template, flash, redirect, session
from . import app
from .forms import MyForm
from .. import clf_path

import pickle
import sys

clf, vec = pickle.load(open(clf_path, 'rb'))
print('read clf %s' % str(clf))
print('read vec %s' % str(vec))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = MyForm()
	result = None
	if form.validate_on_submit():
		input_field = form.input_field.data
		flash(input_field)
		return render_template('myform.html', title='', form=form)
		#return redirect('/index')
	return render_template('myform.html', title='', form=form)
