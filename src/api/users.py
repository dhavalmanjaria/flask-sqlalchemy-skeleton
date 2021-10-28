from flask import Blueprint, jsonify, request
from jinja2 import TemplateNotFound
import requests

users = Blueprint('users', __name__)


@users.route('/get/<id>', methods=['GET'])
@admins_only
def get_id(id):

	# Delegate handling of this function to another function that
	# can be called outside of a request context
	try:
		response_template = handle_get_id(request.json, id)
		return jsonify(response_template.to_dict())
	except Exception as ex:
		log.exception(ex)
