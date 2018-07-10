from models.event import Event
from models.model import db
from sqlalchemy.orm import relationship


class Notifications(db.Model):
    __tablename__ = 'Notifications'

    notif_id = db.Column(db.Integer, primary_key = True)
    timeofupdate = db.Column(db.String(8))
    event_id = db.Column(db.Integer,db.ForeignKey(Event.event_id), nullable = False)
    notif= db.Column(db.String(4096), nullable=False)


    notif_rel = relationship('Event')
