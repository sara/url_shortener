from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)
app.secret_key = "xyz"
app.config['MONGODB_SETTINGS'] = {'db' : 'websites'}
db = MongoEngine(app)
from app import views