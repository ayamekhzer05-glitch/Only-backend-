from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.models.user import User
        from app.models.student import Student
        from app.models.company import Company
        from app.models.skill import Skill
        from app.models.student_skill import StudentSkill
        from app.models.internship_offer import InternshipOffer
        from app.models.offer_skill import OfferSkill
        from app.models.application import Application
        from app.models.notification import Notification

        db.create_all()

        from app.routes.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/api/auth')

    migrate.init_app(app, db)
    return app