# Create a "fortune cookie based on name and date."
from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config
import logging
from data.models import *
from data import dbapi

log = logging.getLogger('console')

app = Flask(__name__, static_url_path='')

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
@app.route('/<path>')
def index(path=None):

    log.info("PATH: " + str(path))
    if path is not None:
        if '.js' in path or '.css' in path:
            return send_from_directory('html', path)

    return send_from_directory('html', 'index.html')



if __name__ == "__main__":
    app.run(debug=True, host=config.flask_host, port=config.flask_port)
