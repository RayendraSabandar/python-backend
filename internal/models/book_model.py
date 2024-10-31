from database.database import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, index=True)
    description = db.Column(db.String(120), nullable=False, index=True)
    publish_date = db.Column(db.DateTime, nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False, index=True)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()