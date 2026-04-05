from flask import current_app
from app import db

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey('internship_offers.id'), nullable=False)
    status = db.Column(db.String(30))
    applied_at = db.Column(db.DateTime, default=db.func.now())
    agreement_pdf = db.Column(db.Text)