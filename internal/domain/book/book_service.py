from .book_repository import BookRepository
from internal.models.book_model import Book

class BookService:
    @staticmethod
    def create(request_body):
        try:
            BookRepository.create(Book(
                title= request_body['title'],
                description= request_body['description'],
                publish_date= request_body['publish_date'],
                author_id= request_body['author_id']
            ))
        
        except Exception as e:
            raise e
    
    @staticmethod
    def list():
        return BookRepository.list()
    
    @staticmethod
    def find_by_id(id):
        return BookRepository.find_by_id(id)