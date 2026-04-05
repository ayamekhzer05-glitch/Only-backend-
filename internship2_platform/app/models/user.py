from flask import current_app
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20))
    phoneNumber = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.now())

    student = db.relationship('Student', backref='user', uselist=False)
    company = db.relationship('Company', backref='user', uselist=False)
    notifications = db.relationship('Notification', backref='user', lazy=True)