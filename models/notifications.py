from models.model import db

class Notifications(db.Model):
    __tablename__ = 'Notifications'

    notificationId = db.Column(db.String(10), primary_key = True)
    notificationTitle = db.Column(db.String(100), nullable = False)
    notificationDetails = db.Column(db.String(4096), nullable = True)
    eventId = db.Column(db.Integer, nullable=False)
    notificationType = db.Column(db.String(10), nullable = False)
