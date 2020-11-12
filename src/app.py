# Create a "fortune cookie based on name and date."
from flask import Flask, jsonify, send_from_directory, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_cors import CORS
import config
import logging
import os
from data.models import *
from data import dbapi, init_db
from api import v1
from views import views

log = logging.getLogger('console')

app = Flask(__name__, static_folder=os.path.abspath('/static'), static_url_path='')

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

root_dir = os.path.dirname(os.getcwd())

def create_app():
    with app.app_context():
        app.register_blueprint(views)


if __name__ == "__main__":
    create_app()
    init_db(app)
    app.run(debug=True, host=config.flask_host, port=config.flask_port)
