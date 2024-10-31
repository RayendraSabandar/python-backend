from database.database import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    bio = db.Column(db.String(120), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False, index=True)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True, index=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()

    # relation
    books = db.relationship('Book', backref='author', lazy=True)