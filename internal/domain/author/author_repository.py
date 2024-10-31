from database.database import db
from internal.models.author_model import Author
from sqlalchemy import and_

class AuthorRepository:
    @staticmethod
    def create(author):
        db.session.add(author)
        db.session.commit()

    @staticmethod
    def list(payload):
        query = Author.query.filter_by(
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
    def find_by_id(id):
        return db.get_or_404(Author, id)
    
    @staticmethod
    def update(author):
        db.session.commit()
        return author