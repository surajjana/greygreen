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

	cur = db.greygreen.insert_one({"r_id": int(r_id), "time": r_time, "rating": int(rating)})

	return '{"status": "OK"}'

@app.route('/data')
def data():
	return template('templates/index.tpl')

@app.route('/json_data')
def json_data():
	cur = db.greygreen.find()
	data = json.loads(dumps(cur))

	res = [{'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 0'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 1'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 2'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 3'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 4'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 5'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 6'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 7'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 8'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 9'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 10'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 11'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 12'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 13'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 14'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 15'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 16'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 17'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 18'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 19'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 20'}]

	for i in range(0, len(data)):
		if(data[i]['r_id'] == 0):
			res[0]['x'].append(data[i]['time'])
			res[0]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 1):
			res[1]['x'].append(data[i]['time'])
			res[1]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 2):
			res[2]['x'].append(data[i]['time'])
			res[2]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 3):
			res[3]['x'].append(data[i]['time'])
			res[3]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 4):
			res[4]['x'].append(data[i]['time'])
			res[4]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 5):
			res[5]['x'].append(data[i]['time'])
			res[5]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 6):
			res[6]['x'].append(data[i]['time'])
			res[6]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 7):
			res[7]['x'].append(data[i]['time'])
			res[7]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 8):
			res[8]['x'].append(data[i]['time'])
			res[8]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 9):
			res[9]['x'].append(data[i]['time'])
			res[9]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 10):
			res[10]['x'].append(data[i]['time'])
			res[10]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 11):
			res[11]['x'].append(data[i]['time'])
			res[11]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 12):
			res[12]['x'].append(data[i]['time'])
			res[12]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 13):
			res[13]['x'].append(data[i]['time'])
			res[13]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 14):
			res[14]['x'].append(data[i]['time'])
			res[14]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 15):
			res[15]['x'].append(data[i]['time'])
			res[15]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 16):
			res[16]['x'].append(data[i]['time'])
			res[16]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 17):
			res[17]['x'].append(data[i]['time'])
			res[17]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 18):
			res[18]['x'].append(data[i]['time'])
			res[18]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 19):
			res[19]['x'].append(data[i]['time'])
			res[19]['y'].append(data[i]['rating'])
		elif(data[i]['r_id'] == 20):
			res[20]['x'].append(data[i]['time'])
			res[20]['y'].append(data[i]['rating'])

	return json.dumps(res)