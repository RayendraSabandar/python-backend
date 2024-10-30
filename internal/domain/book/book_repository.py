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
    
    @staticmethod
    def list_by_author_id(author_id):
        return Book.query.filter_by(
            deleted_at = None,
            author_id = author_id
        )
    
    @staticmethod
    def find_by_id(id):
        return db.get_or_404(Book, id)
    
    @staticmethod
    def update(author):
        db.session.commit()
        return author