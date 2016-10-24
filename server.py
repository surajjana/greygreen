import json
from bottle import Bottle, run, route, static_file, request, response, template
import requests
from pymongo import MongoClient
from bson.json_util import dumps
import pymongo
import requests
import time
import urlparse
import os

app = Bottle(__name__)

client = MongoClient('mongodb://52.34.226.223:27017/test')
db = client.test

@app.route('/')
def root():
	return 'Grey Green Restaurant Server Started'
	# res = {'data':{'x': ['2013-10-04 13:00:00', '2013-10-04 15:30:00', '2013-10-04 22:30:00'],'y': [1, 3, 4],'type': 'scatter','name': 'Restaurant 1'}}
	# # res = {"res": res}
	# #print type(res)
	# return template('templates/index.tpl', **res)

# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static/img')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/add_data')
def add_data():
	return template('templates/add_data.tpl')

@app.post('/add_data')
def add_data_post():
	r_id = request.forms.get('r_id')
	r_time = request.forms.get('r_time')
	rating = request.forms.get('rating')

	cur = db.greygreen.insert_one({"r_id": int(r_id), "time": r_time, "rating": rating})

	return '{"status": "OK"}'

@app.route('/data')
def data():
	return template('templates/index.tpl')

@app.route('/json_data')
def json_data():
	cur = db.greygreen.find({"r_id": 0})
	data = json.loads(dumps(cur))

	return json.dumps(data)