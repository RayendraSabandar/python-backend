from database.database import db
from internal.models.author_model import Author

class AuthorRepository:
    @staticmethod
    def list():
        return Author.query.all()