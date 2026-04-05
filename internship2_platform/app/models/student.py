from flask import current_app
from app import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    university = db.Column(db.String(255))
    field_of_study = db.Column(db.String(255))
    degree = db.Column(db.String(100))
    year = db.Column(db.Integer)
    github_link = db.Column(db.String(255))
    portfolio_link = db.Column(db.String(255))
    linkedin = db.Column(db.String(255))
    cv = db.Column(db.String(255))
    placement_status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.now())

    skills = db.relationship('StudentSkill', backref='student', lazy=True)
    applications = db.relationship('Application', backref='student', lazy=True)