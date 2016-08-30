from app import app, db
from flask import Flask, flash, render_template, request, redirect, url_for
from urllib2 import urlopen
from models import Pairs

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method =='POST':
		long_url = request.form["original"]
		short_url = request.form["short"]
		modified_long_url = validate(long_url)
		if modified_long_url != None and len(short_url) < 11:
			new_url = Pairs(full = modified_long_url, short = short_url)
			new_url.save()
			return modified_long_url + " " + short_url
			
			#return render_template("confirm.html", longurl = modified_long_url, shorturl = short_url)
		else:
			return redirect(url_for('.error'))#render_template("error.html")
	
	if request.method == 'GET':
		return render_template("homepage.html")

@app.route('/error', methods = ['GET', 'POST'])
def error():
	if request.method == 'POST':
		return redirect(url_for('index'))
	if request.method == 'GET':
		return render_template('error.html')

@app.route('/short/<website>', methods =['GET'])
def shortcut(website):
	if request.method == 'GET':
		#return render_template("error.html")
		#website = Pairs.objects()
		merp = Pairs.objects(short = website)
		target = merp[0].full
		#return target#merp[0].full
		#target = merp.long
		return redirect(target)
@app.route('/confirm', methods = ['GET'])
def confirm():
	if request.method =='GET':
		return render_template("confirm.html")


#check if if's a real url
def validate(long_url):
	#EXTRA: add on http/https to input
	try:
		file = urlopen(long_url)
		modified_long_url = file.geturl()
	except:
		modified_long_url = None
		return None
	return modified_long_url
