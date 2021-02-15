from flask import render_template
from flask import Flask, request, jsonify
from model import Model
import os

Model = Model()

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')


# API Route
@app.route('/api/text', methods=['GET','POST'])
def Text():
	if request.form:
		text = request.form['text']
		return Model.result_json(text)
	else:
		return Model.result_json()



if __name__ == '__main__':
	app.run(debug = True)