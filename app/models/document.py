from datetime import datetime

from app.extensions import db


class Document(db.Model):

    __tablename__ = "documents"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    file_type = db.Column(
        db.String(50),
        nullable=False
    )

    upload_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(50),
        default="uploaded"
    )

    def __repr__(self):
        return f"<Document {self.file_name}>"