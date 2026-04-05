from flask import current_app
from app import db
class InternshipOffer(db.Model):
    __tablename__ = 'internship_offers'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    type = db.Column(db.String(50))
    technology = db.Column(db.String(255))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.now())
    deadline = db.Column(db.Date)

    skills = db.relationship('OfferSkill', backref='offer', lazy=True)
    applications = db.relationship('Application', backref='offer', lazy=True)