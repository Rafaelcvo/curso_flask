from flask import Flask
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
=======

app = Flask(__name__)
>>>>>>> 4ece540f7f1b0317cab9880a0f37eacf8c1344a6

from app.controllers import default
