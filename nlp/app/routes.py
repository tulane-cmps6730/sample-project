from flask import render_template, flash, redirect, session
from . import app
from .forms import MyForm
from .. import clf_path

import pickle
import sys

clf, vec = pickle.load(open(clf_path, 'rb'))
print('read clf %s' % str(clf))
print('read vec %s' % str(vec))
labels = ['liberal', 'conservative']

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = MyForm()
	result = None
	if form.validate_on_submit():
		input_field = form.input_field.data
		X = vec.transform([input_field])
		pred = clf.predict(X)[0]
		proba = clf.predict_proba(X)[0].max()
		# flash(input_field)
		return render_template('myform.html', title='', form=form, 
								prediction=labels[pred], confidence='%.2f' % proba)
		#return redirect('/index')
	return render_template('myform.html', title='', form=form, prediction=None, confidence=None)
