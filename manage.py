from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from create_app import app
from models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

manager.run()