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

#client = MongoClient('mongodb://52.34.226.223:27017/test')
client = MongoClient()
db = client.test

@app.route('/')
def root():
	return 'BL Python Server'
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

@app.post('/heymedy_ping')
def heymedy_ping():
        name = request.forms.get('name')
        email = request.forms.get('email')
        phone = request.forms.get('phone')

        cur = db.heymedy.insert_one({"name": name, "email": email, "phone": phone})

        return '{"status": "OK"}'

@app.route('/hosp_reg/<data>')
def hosp_reg(data):

	try:
		cur = db.merchant_hosp.insert_one(json.loads(data))
	except:
		return '{"status": "NA"}'
	else:
		return '{"status": "OK"}'

@app.post('/upload_logo')
def upload_logo():
	data = request.files.data
	print data
	try:
		if(data and data.file):
			data.save('/home/suraj/Pictures/test.png',overwrite=True)
	except:
		return 'Failure'
	else:
		return 'Success'

@app.post('/base64_img')
def base64_img():
	return request.forms.get('data')
	# imgData = b"'"+data+"'"
	# try:
	# 	fh = open("img_data/"+filename, "wb")
	# 	fh.write(imgData.decode('base64'))
	# except:
	# 	return '{"status": "Error"}'
	# else:
	# 	fh.close()
	# 	return '{"status": "OK"}'


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

@app.route('/json')
def json_test():
	cur = db.greygreen.find()
	data = json.loads(dumps(cur))

	#res = [{'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 0'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 1'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 2'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 3'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 4'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 5'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 6'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 7'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 8'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 9'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 10'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 11'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 12'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 13'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 14'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 15'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 16'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 17'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 18'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 19'}, {'x': [], 'y': [], 'type': 'scatter', 'name': 'Restaurant 20'}]
	res = [{'label': 'Restaurant 1','strokeColor': '#A31515','data': []}]

	for i in range(0, len(data)):
		if(data[i]['r_id'] == 1):
			res[0]['data'].append({'x': data[i]['time'], 'y': data[i]['rating']})

	return json.dumps(res)

client_1 = MongoClient('mongodb://52.34.226.223:27017/krispypapad')
db_1 = client_1.krispypapad

@app.route('/articles')
def read_all():
    cur = db_1.articles.find()
    return dumps(cur)

@app.route('/articles/<id>')
def read_by_id(id):
    cur = db_1.articles.find({"id": int(id)})
    return dumps(cur)

@app.route('/update')
def update_articles():
    id_1 = request.forms.get('id')
    title = request.forms.get('title')
    content_1 = request.forms.get('content_1')
    content_2 = request.forms.get('content_2')
    author = request.forms.get('author')
    powered_by = request.forms.get('powered_by')
    source_name = request.forms.get('source_name')
    image = request.forms.get('image')
    original_link = request.forms.get('original_link')
    likes = request.forms.get('likes')
    shares = request.forms.get('shares')
    tags = request.forms.get('tags')
    status = request.forms.get('status')
    time_stamp = time.time()

    

    cur = db_1.articles.update_one({"id": int(id_1)},{"$set": {"title": title, "content_1": content_1, "content_2": content_2, "author": author, "powered_by": powered_by, "source_name": source_name, "image": image, "originak_link":original_link, "likes": likes, "shares": shares, "tags": tags, "status": status, "time_stamp": time_stamp}})
    #cur = db_1.articles.update({"id": int(id)},{"$set": {"title": title}})
    #return json.dumps({'id': int(id), 'matched_count': cur.matched_count, 'modified_count': cur.modified_count})
    return dumps(cur)

@app.post('/login_test')
def login_check():
	username = request.forms.get('uname')
	pwd = request.forms.get('pwd')

	print username
	print pwd

	if (username == 'admin' and pwd == 'admin'):
		return json.dumps({'status': 'ok', 'username': username})
	else:
		return json.dumps({'status': 'error'})