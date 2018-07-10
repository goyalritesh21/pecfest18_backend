'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
#
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:hello@localhost/pecfest'
#initialize a db object
db=SQLAlchemy(app)'''
from models.model import db

class Event(db.Model):
	__tablename__ = 'Event'

	event_id = db.Column(db.Integer, primary_key=True, nullable=False)
	event_name = db.Column(db.String(100), unique=True, nullable=False)
	club_id= db.Column(db.String(10), default=0)
	day=db.Column(db.Integer)
	timeofevent=db.Column(db.String(8),nullable=False)
	venue=db.Column(db.String(20))


	def __repr__(self):
		return 'Event: <' + self.event_name + '>'


	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


'''import pymysql
import requests
connect=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='pecfest')
a=connect.cursor()

sql= 'select * from `form`;'
a.execute(sql)
countrow=a.execute(sql)

print("number of rows :",countrow)

data=a.fetchone()
print(data)

resp=requests.get('http://api.open-notify.org/iss-pass')
print(resp.status_code)'''