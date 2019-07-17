import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MONGO_URI = "mongodb://localhost:27017/myDatabase"
#MONGO_URI = 'mongodb://admin:admin@testespython-shard-00-00-yvcc0.mongodb.net:27017'
SECRET_KEY = 'eae_b_b'