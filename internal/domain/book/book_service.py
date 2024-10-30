from .book_repository import BookRepository
from internal.models.book_model import Book

class BookService:
    @staticmethod
    def list():
        return BookRepository.list()