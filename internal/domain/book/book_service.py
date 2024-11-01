from .book_repository import BookRepository
from internal.models.book_model import Book
from datetime import datetime

class BookService:
    @staticmethod
    def create(db, request_body):
        try:
            BookRepository.create(db, Book(
                title= request_body['title'],
                description= request_body['description'],
                publish_date= request_body['publish_date'],
                author_id= request_body['author_id']
            ))
        
        except Exception as e:
            raise e
    
    @staticmethod
    def list(db, payload):
        return BookRepository.list(db, payload)
    
    @staticmethod
    def list_by_author_id(db, author_id, page, limit):
        return BookRepository.list_by_author_id(db, author_id, page, limit)
    
    @staticmethod
    def find_by_id(db, id):
        return BookRepository.find_by_id(db, id)
    
    @staticmethod
    def update(db, id, request_body):
        try:
            book = BookRepository.find_by_id(db, id)
            book.title = request_body['title']
            book.description = request_body['description']
            book.publish_date = request_body['publish_date']
            book.author_id = request_body['author_id']
            BookRepository.update(db, book)
            return book
        except Exception as e:
            raise e
        
    @staticmethod
    def soft_delete(db, id):
        try:
            author = BookRepository.find_by_id(db, id)
            author.deleted_at = datetime.now()
            BookRepository.update(db, author)
            return author
        except Exception as e:
            raise e
