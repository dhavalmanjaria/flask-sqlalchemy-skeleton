from data import init_db
from app import app, create_app

# These need to be called outside the main block
wsgi_app = create_app()
init_db(wsgi_app)

if __name__ == "__main__":

    app.run()

