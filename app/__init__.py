from flask import Flask

from app.config.settings import Config
from app.extensions import db

from app.blueprints.upload_routes import upload_bp
from app.blueprints.chat_routes import chat_bp

from app.models import (
    User,
    Document,
    ChatHistory
)


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(upload_bp)
    app.register_blueprint(chat_bp)

    return app