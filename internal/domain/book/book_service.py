from .book_repository import BookRepository
from internal.models.book_model import Book
from datetime import datetime

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
    
    @staticmethod
    def update(id, request_body):
        try:
            book = BookRepository.find_by_id(id)
            book.title = request_body['title']
            book.description = request_body['description']
            book.publish_date = request_body['publish_date']
            book.author_id = request_body['author_id']
            BookRepository.update(book)
            return book
        except Exception as e:
            raise e
        
    @staticmethod
    def soft_delete(id):
        try:
            author = BookRepository.find_by_id(id)
            author.deleted_at = datetime.now()
            BookRepository.update(author)
            return author
        except Exception as e:
            raise e
