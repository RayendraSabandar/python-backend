from internal.domain.book.book_service import BookService
from transport.http.response.response import Response
from flask import request
from werkzeug.exceptions import NotFound


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
    
    @staticmethod
    def find_by_id(book_id):
        try:
            res = BookService.find_by_id(book_id)
            return {
                    "id": res.id,
                    "title": res.title,
                    "description": res.description,
                    "publish_date": res.publish_date,
                    "author_id": res.author_id
                } 
        
        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "book not found")
            
            return Response.handleErr(e, None)
        
    @staticmethod
    def update(book_id):
        try:
            request_body = request.json
            res = BookService.update(book_id, request_body)
            return {
                "id": res.id,
                "title": res.title,
                "description": res.description,
                "publish_date": res.publish_date,
                "author_id": res.author_id
            } 

        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "book not found")
            
            return Response.handleErr(e, None)