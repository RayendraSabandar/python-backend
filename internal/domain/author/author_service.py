from .author_repository import AuthorRepository
from internal.models.author_model import Author
from datetime import datetime

class AuthorService:
    @staticmethod
    def create(db, request_body):
        try:
            AuthorRepository.create(db, Author(
                name= request_body['name'],
                bio= request_body['bio'],
                birth_date= request_body['birth_date']
            ))
        
        except Exception as e:
            raise e

    @staticmethod
    def list(db, payload):
        try:
            return AuthorRepository.list(db, payload)
        
        except Exception as e:
            raise e
            
    
    @staticmethod
    def find_by_id(db, id):
        return AuthorRepository.find_by_id(db, id)
    
    @staticmethod
    def update(db, id, request_body):
        try:
            author = AuthorRepository.find_by_id(db, id)
            author.name = request_body['name']
            author.bio = request_body['bio']
            author.birth_date = request_body['birth_date']
            AuthorRepository.update(db, author)
            return author
        except Exception as e:
            raise e
        
    @staticmethod
    def soft_delete(db, id):
        try:
            author = AuthorRepository.find_by_id(db, id)
            author.deleted_at = datetime.now()
            AuthorRepository.update(db, author)
            return author
        except Exception as e:
            raise e
