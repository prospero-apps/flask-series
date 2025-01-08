from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.age}'