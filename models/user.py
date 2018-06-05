from models.model import db

class Participant(db.Model):
	'''
		Contain details of a user.
	'''

	__tablename__ = 'Participant'

	pecfestId = db.Column(db.String(10), primary_key=True)
	firstName = db.Column(db.String(256), nullable=False)
	lastName = db.Column(db.String(256), nullable = False)
	collegeName = db.Column(db.String(256), nullable=False)
	emailId = db.Column(db.String(100), nullable=False)
	mobileNumber = db.Column(db.String(10), nullable=False)
	gender = db.Column(db.String(10), nullable=False)
	accomodation = db.Column(db.String(255), nullable=False)
	verified = db.Column(db.Integer, nullable=False)
	smsCounter = db.Column(db.Integer, default=0)

	def __repr__(self):
		return 'User: <' + self.pecfestId + ':' + self.name + '>'

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


