from models.model import db
from werkzeug.security import generate_password_hash, check_password_hash


class Participant(db.Model):

    __tablename__ = 'Participant'

    pecfestId = db.Column(db.String(10), primary_key=True)
    firstName = db.Column(db.String(256), nullable=False)
    lastName = db.Column(db.String(256), nullable = False)
    collegeName = db.Column(db.String(256), nullable=False)
    emailId = db.Column(db.String(100), nullable=False)
    mobileNumber = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    accomodation = db.Column(db.String(10), nullable=False)
    verified = db.Column(db.Integer, nullable=False)
    smsCounter = db.Column(db.Integer, default=0)
    password = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return 'User: <' + self.pecfestId + ':' + self.password +'>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password,password)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


