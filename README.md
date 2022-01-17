# flask-sqlalchemy-skeleton

This is an empty python tempalte app that uses Flask with Flask Blueprint and SQLAlchemy along with other bells and whistles configured properly so that other apps can be built on top of it.

### Running the application

#### Gunicorn

Run the file `src/scripts/run_app.sh`. 

Note that if you are uploading it to a linux server from a windows machine, you'll have to use the dos2unix utility (which will need to be installed on the Linux machine).


#### Docker

`sudo docker build -t <your_tag> .`

`sudo docker run --rm -p <your_ports>:4000 -t <your_tag>`

#### Manually

Create a virtual environment

`virtualenv venv`

Install dependencies

`pip install -r requirements.txt`

Run with gunicorn

`gunicorn -c gunicorn-config.py wsgi:app`

### Key features

* SQLAlchemy condfigured to use sqlite, but also has postgres connection strings available

* Blueprint configured to serve endpoints using the path /api/v1/_endpoints_. A test endpoint is available at /api/v1/execute

* Home page and static files served using flask.

* Logging config that covers file logging, console logging and both.

* `init_engine_for_shell.py` file that allows users to use SQLAlchemy models connected to the DB in a python shell

* Basic gunicorn configuration

* Dockerfile 



