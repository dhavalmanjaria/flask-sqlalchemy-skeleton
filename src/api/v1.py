from flask import Blueprint, jsonify, request
from jinja2 import TemplateNotFound
import requests

v1 = Blueprint('v1', __name__)

@v1.route('/execute', methods=['GET', 'POST'])
def execute():

	# HTTP Method
	# WebAPI 
	if request.method == 'GET':
		# DO GET Stuff
		pass

	# r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
	# client_data = r.json()

	# print(client_data)

	data = request.json

	return_data = {
		"user": 10,
		"role": "B12"
	}

	return jsonify(response='ok', data=return_data)