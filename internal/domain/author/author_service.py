from .author_repository import AuthorRepository
from internal.models.author_model import Author
from datetime import datetime

class AuthorService:
    @staticmethod
    def create(request_body):
        try:
            AuthorRepository.create(Author(
                name= request_body['name'],
                bio= request_body['bio'],
                birth_date= request_body['birth_date']
            ))
        
        except Exception as e:
            raise e

    @staticmethod
    def list(payload):
        try:
            return AuthorRepository.list(payload)
        
        except Exception as e:
            raise e
            
    
    @staticmethod
    def find_by_id(id):
        return AuthorRepository.find_by_id(id)
    
    @staticmethod
    def update(id, request_body):
        try:
            author = AuthorRepository.find_by_id(id)
            author.name = request_body['name']
            author.bio = request_body['bio']
            author.birth_date = request_body['birth_date']
            AuthorRepository.update(author)
            return author
        except Exception as e:
            raise e
        
    @staticmethod
    def soft_delete(id):
        try:
            author = AuthorRepository.find_by_id(id)
            author.deleted_at = datetime.now()
            AuthorRepository.update(author)
            return author
        except Exception as e:
            raise e
