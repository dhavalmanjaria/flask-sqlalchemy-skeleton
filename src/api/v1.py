from flask import Blueprint, jsonify, request
from jinja2 import TemplateNotFound

v1 = Blueprint('v1', __name__)

@v1.route('/execute', methods=['GET', 'POST'])
def execute():

	# HTTP Method
	# WebAPI 
	if request.method == 'GET':
		# DO GET Stuff
		pass


	data = request.json

	return jsonify(response='ok', user_data=data)