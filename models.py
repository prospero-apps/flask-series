from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile = db.Column(db.String)
    role = db.Column(db.String)

    def __repr__(self):
        return f'{self.username} ({self.role})'
    
    def get_id(self):
        return self.id