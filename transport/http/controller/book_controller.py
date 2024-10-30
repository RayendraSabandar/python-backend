from internal.domain.book.book_service import BookService
from transport.http.response.response import Response
from flask import request

class BookController:
    @staticmethod
    def create():
        try:
            request_body = request.json
            BookService.create(request_body)
            return Response.handleResponse(None)
        
        except Exception as e:
            return Response.handleErr(e, None)
        
    @staticmethod
    def list():
        books = BookService.list()
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