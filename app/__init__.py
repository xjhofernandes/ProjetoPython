from flask import Flask
from flask_pymongo import PyMongo
from flask_script import Manager
from flask_login import LoginManager

app = Flask(__name__) #instância da classe Flask
app.config.from_object('config') #Configuração das Libs

manager = Manager(app) #Flask Script
#manager.add_command('mongo', MigrateCommand)

mongo = PyMongo(app) #PyMongo

#mongo = PyMongo(app, uri="mongodb+srv://admin:admin@testespython-yvcc0.mongodb.net/test?retryWrites=true&w=majority")

lm = LoginManager(app) #LoginManager

from app.models import tables
from app.controllers import default
