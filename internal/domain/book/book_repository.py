from internal.models.book_model import Book
from sqlalchemy.orm import Session
from flask import abort

class BookRepository:
    @staticmethod
    def create(db: Session, book):
        db.add(book)
    
    @staticmethod
    def list(db: Session, payload):
        query = db.query(Book).filter_by(
            deleted_at = None
        )
        if payload.title:
            query = query.filter(Book.title.ilike(f"%{payload.title}%"))
        if payload.description:
            query = query.filter(Book.description.ilike(f"%{payload.description}%"))
        if payload.start_publish_date:
            query = query.filter(Book.publish_date >= payload.start_publish_date)
        if payload.end_publish_date:
            query = query.filter(Book.publish_date <= payload.end_publish_date)
        
        query = query.paginate(
            page= payload.page,
            per_page= payload.limit
        )

        return query.items
    
    @staticmethod
    def list_by_author_id(db: Session, author_id):
        return db.query(Book).filter_by(
            deleted_at = None,
            author_id = author_id
        )
    
    @staticmethod
    def find_by_id(db: Session, id):
        book = db.query(Book).filter_by(
            deleted_at = None,
            id = id
        ).first()
        if book is None:
            abort(404)

        return book
    
    @staticmethod
    def update(db: Session, author):
        return author