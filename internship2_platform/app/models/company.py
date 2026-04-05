from flask import current_app
from app import db

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    company_name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    description = db.Column(db.Text)
    address = db.Column(db.Text)
    logo = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

    offers = db.relationship('InternshipOffer', backref='company', lazy=True)