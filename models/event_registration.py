from models.model import db
from sqlalchemy.orm import relationship

class EventRegistration(db.Model):
	__tablename__ = 'Event_reg'

	pecfestid = db.Column(db.Integer,db.ForeignKey('Pecfestids.id'),primary_key = True ,nullable=False)
	event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'), nullable=False)

	event_id_relation = relationship('Event')

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


