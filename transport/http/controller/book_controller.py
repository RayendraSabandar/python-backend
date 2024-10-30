from internal.domain.book.book_service import BookRepository
from transport.http.response.response import Response

class BookController:
    @staticmethod
    def list():
        books = BookRepository.list()
        res = [
            {
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "publish_date": book.publish_date,
                "author_id": book.author_id
            } 
            for book in books
        ]
        return Response.handleResponse(res)