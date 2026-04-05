from flask import current_app
from app import db

class StudentSkill(db.Model):
    __tablename__ = 'student_skills'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), primary_key=True)

    skill = db.relationship('Skill', backref='student_skills')