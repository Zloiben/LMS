from flask_login import UserMixin
from . import db, create_app


class User(UserMixin, db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    role = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data = db.Column(db.TEXT())

    def __init__(self, name, role, password, email, data):

        self.name = name
        self.password = password
        self.role = role
        self.email = email
        self.data = data

    def __repr__(self):
        return '<User %r>' % self.name


db.create_all(app=create_app())
