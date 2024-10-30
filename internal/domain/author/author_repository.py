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
    
    @staticmethod
    def find_by_id(id):
        return db.get_or_404(Author, id)
    
    @staticmethod
    def update(author):
        db.session.commit()
        return author