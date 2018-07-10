db = None

def pass_param(database):
	global db
	db = database
'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
#
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:hello@localhost/pecfest'
#initialize a db object
db=SQLAlchemy(app)'''
