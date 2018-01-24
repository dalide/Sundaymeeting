from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from random import randint
from flask_sqlalchemy import SQLAlchemy
import os

image_folder = os.path.join('static', 'images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lichengshuaige'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class users(db.Model):
	id = db.Column('user_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(50))
	addr = db.Column(db.String(200))
	zipcode = db.Column(db.String(10))

	def __init__(self, name, city, addr, zipcode):
		self.name = name
		self.city = city
		self.addr = addr
		self.zipcode = zipcode



@app.route("/")
def index():
	filename = os.path.join(image_folder, 'data-scientist.jpg')
	return render_template('index.html', ds_image = filename)

# @app.route('/signuplogin', methods = ['POST','GET'])
# def signuplogin():
# 	return render_template('signuplogin.html')
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html', users = users.query.all())

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         user = users(request.form['name'], request.form['city'],
            request.form['addr'], request.form['zipcode'])
         
         db.session.add(user)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('dashboard'))
   return render_template('signup.html')

@app.route('/login', methods=['POST','GET'])
def login():
	error = None

	if request.method == 'POST':
		if request.form['username'] !='admin' or request.form['password'] !='admin':
			error = 'Invalid username or password. Please try again!'
		else:
			flash('You were successfully logged in')
			return redirect(url_for('dashboard'))

	return render_template('login.html', error=error)





if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)

