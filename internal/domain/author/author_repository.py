from database.database import db
from internal.models.author_model import Author

class AuthorRepository:
    @staticmethod
    def create(author):
        db.session.add(author)
        db.session.commit()

    @staticmethod
    def list():
        return Author.query.all()