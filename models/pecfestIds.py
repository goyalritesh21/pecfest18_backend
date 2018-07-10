from models.model import db

class Pecfestids(db.Model):
	'''
		Contains all registered pecfest IDs
	'''
	__tablename__ = 'Pecfestids'
	id= db.Column(db.Integer, primary_key=True)

	def __repr__(self):
		return 'ID: <' + self.id + '>'

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


