from internal.models.author_model import Author
from sqlalchemy.orm import Session
from flask import abort

class AuthorRepository:
    @staticmethod
    def create(db: Session, author):
        db.add(author)

    @staticmethod
    def list(db: Session, payload):
        query = db.query(Author).filter_by(
            deleted_at = None
        )

        if payload.name:
            query = query.filter(Author.name.ilike(f"%{payload.name}%"))
        if payload.start_birth_date:
            query = query.filter(Author.birth_date >= payload.start_birth_date)
        if payload.end_birth_date:
            query = query.filter(Author.birth_date <= payload.end_birth_date)

        return query.all()
    
    @staticmethod
    def find_by_id(db: Session, id):
        author = db.query(Author).filter_by(
            deleted_at = None,
            id = id
        ).first()
        if author is None:
            abort(404)

        return author
    
    @staticmethod
    def update(db: Session, author):
        return author