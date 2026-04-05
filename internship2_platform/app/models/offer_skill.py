from flask import current_app
from app import db

class OfferSkill(db.Model):
    __tablename__ = 'offer_skills'
    offer_id = db.Column(db.Integer, db.ForeignKey('internship_offers.id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), primary_key=True)

    skill = db.relationship('Skill', backref='offer_skills')