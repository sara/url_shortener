from app import db

class Pairs (db.Document):
	long = db.StringField(required = True)
	short = db.StringField(required = True)
	#set unique to true once you get the basic working