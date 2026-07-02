from datetime import datetime

from database.db import db


class Document(db.Model):

    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    filepath = db.Column(db.String(500), nullable=False)

    upload_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(30),
        default="Uploaded"
    )

    pages = db.Column(
        db.Integer,
        default=0
    )