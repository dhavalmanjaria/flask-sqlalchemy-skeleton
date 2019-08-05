from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from data import connection
import config


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
