from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__) #instância da classe Flask
app.config.from_object('config') #Configuração das Libs

mongo = PyMongo(app)
#mongo = PyMongo(app, uri="mongodb+srv://admin:admin@testespython-yvcc0.mongodb.net/test?retryWrites=true&w=majority")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager(app)

from app.models import tables
from app.controllers import default
