from logging.config import dictConfig

# Flask
flask_host = "127.0.0.1"
flask_port = "5000"
debug = True

# postgres
postgres_username = 'postgres'
postgres_password = 'password'
db_name = "fortune-cookie"
postgres_host = "127.0.0.1"
postgres_port = "5432"

sqlalchemy_database_uri = "sqlite:///test.db"


# For a good understanding on config
# See: https://www.toptal.com/python/in-depth-python-logging#:~:text=There%20are%20six%20log%20levels,particularity%20will%20be%20addressed%20next.
# Logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s',
        },
        'info': {
            'format': '[%(asctime)s]: %(message)s',
            'datefmt': '%H:%M:%S'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log'
        },
        'debugfilehandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default'
        },
        'consoledebughandler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'consolehandler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'info'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['debugfilehandler', 'consolehandler'],
            'level': 'DEBUG',
            'propogate': True,
        },
        'console': {
            'handlers': ['consoledebughandler', 'debugfilehandler'],
            'level': 'INFO',
            'propogate': True
        }
    }
}

dictConfig(LOGGING_CONFIG)
