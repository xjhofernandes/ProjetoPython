from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instância da classe Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default