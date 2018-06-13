from models.model import db
from sqlalchemy.orm import relationship


class Notifications(db.Model):
    __tablename__ = 'Notifications'

    notificationId = db.Column(db.String(10), primary_key = True)
    notificationTitle = db.Column(db.String(100), nullable = False)
    notificationDetails = db.Column(db.String(4096), nullable = True)
    eventId = db.Column(db.Integer, db.ForeignKey('Event.eventId'), nullable=False)
    notificationType = db.Column(db.String(10), nullable = False)

    notif_rel = relationship('Event')
