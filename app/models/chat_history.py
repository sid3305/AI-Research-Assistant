from datetime import datetime

from app.extensions import db


class ChatHistory(db.Model):

    __tablename__ = "chat_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    question = db.Column(
        db.Text,
        nullable=False
    )

    answer = db.Column(
        db.Text,
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<ChatHistory {self.id}>"