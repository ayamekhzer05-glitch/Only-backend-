from flask import current_app
from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255))
    message = db.Column(db.Text)
    type = db.Column(db.String(20))
    related_to = db.Column(db.String(20))
    related_id = db.Column(db.String(36))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())