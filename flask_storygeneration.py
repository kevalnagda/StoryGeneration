from flask import Flask, render_template, url_for, flash, redirect
from forms import ThemeForm
from storygeneration.combined import generateStory
app = Flask(__name__)

app.config['SECRET_KEY'] = '5bd61c5f5aadc9cae395915a8753d577'

@app.route("/", methods=['GET','POST'])
def theme():
	form = ThemeForm()
	if form.validate_on_submit():
		result = generateStory(form.theme.data, form.prompt.data)
		return render_template('results.html', result=result)
	return render_template('theme.html', form=form)

@app.route("/results")
def results():
	return render_template('results.html', result=result)


if '__name__' == '__main':
	app.run(debug=True)
