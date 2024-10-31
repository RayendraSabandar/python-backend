from database.database import db
from internal.models.book_model import Book
from sqlalchemy.orm import Session

class BookRepository:
    @staticmethod
    def create(book):
        db.session.add(book)
        db.session.commit()
    
    @staticmethod
    def list(payload):
        query = Book.query.filter_by(
            deleted_at = None
        )
        print(f"payload.title: {payload.title}")
        print(f"payload.description: {payload.description}")
        print(f"payload.start_publish_date: {payload.title}")
        print(f"payload.end_publish_date: {payload.end_publish_date}")
        if payload.title:
            query = query.filter(Book.title.ilike(f"%{payload.title}%"))
        if payload.description:
            query = query.filter(Book.description.ilike(f"%{payload.description}%"))
        if payload.start_publish_date:
            query = query.filter(Book.publish_date >= payload.start_publish_date)
        if payload.end_publish_date:
            query = query.filter(Book.publish_date <= payload.end_publish_date)

        return query.all()
    
    @staticmethod
    def list_by_author_id(db: Session, author_id):
        return db.query(Book).filter_by(
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