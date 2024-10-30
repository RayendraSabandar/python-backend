from database.database import db
from internal.models.book_model import Book

class BookRepository:
    @staticmethod
    def create(author):
        db.session.add(author)
        db.session.commit()
    
    @staticmethod
    def list():
        return Book.query.filter_by(
            deleted_at = None
        )