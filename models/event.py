from models.model import db

class Event(db.Model):

	__tablename__ = 'Event'

	eventId = db.Column(db.Integer, primary_key=True, nullable=False)
	Name = db.Column(db.String(100), unique=True, nullable=False)
	Coordinators = db.Column(db.String(4096))
	Location = db.Column(db.String(200))
	day = db.Column(db.Integer)
	time = db.Column(db.String(50))
	prize = db.Column(db.String(256))
	minSize = db.Column(db.Integer, default=0)
	maxSize = db.Column(db.Integer, default=0)

	eventType = db.Column(db.Integer, nullable=False)
	category = db.Column(db.Integer, default=0)
	clubId = db.Column(db.String(10), default=0)
	details = db.Column(db.String(4096))
	shortDescription = db.Column(db.String(300))

	imageUrl = db.Column(db.String(255), default='')
	rulesList = db.Column(db.String(4096))

	pdfUrl = db.Column(db.String(255), nullable=False)
	# eventWinners = db.Column(db.String(4096))

	def __repr__(self):
		return 'Event: <' + self.eventName + '>'

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


