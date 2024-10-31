from internal.domain.book.book_service import BookService
from internal.domain.book.book_payload import ListPayload
from transport.http.response.response import Response
from flask import request
from werkzeug.exceptions import NotFound
from dateutil import parser
from database.database import transaction

class BookController:
    @staticmethod
    def create():
        try:
            with transaction() as db:
                request_body = request.json
                BookService.create(db, request_body)
                return Response.handleResponse(None)
        
        except Exception as e:
            return Response.handleErr(e, None)
        
    @staticmethod
    def list():
        try:
            with transaction() as db:
                filter_title = request.args.get('title', None)
                filter_description = request.args.get('description', None)
                start_publish_date_str = request.args.get('start_publish_date', None)
                end_publish_date_str = request.args.get('end_publish_date', None)
                start_publish_date = parser.isoparse(start_publish_date_str) if start_publish_date_str else None
                end_publish_date = parser.isoparse(end_publish_date_str) if end_publish_date_str else None
                
                books = BookService.list(db, ListPayload(
                    title= filter_title,
                    description= filter_description,
                    start_publish_date= start_publish_date,
                    end_publish_date= end_publish_date
                ))
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
        
        except Exception as e:
            return Response.handleErr(e, None)
    
    @staticmethod
    def find_by_id(book_id):
        try:
            with transaction() as db:
                res = BookService.find_by_id(db, book_id)
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
            with transaction() as db:
                request_body = request.json
                res = BookService.update(db, book_id, request_body)
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
    def delete(book_id):
        try:
            with transaction() as db:
                BookService.soft_delete(db, book_id)
                return Response.handleResponse(None)
        
        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "book not found")
            
            return Response.handleErr(e, None)