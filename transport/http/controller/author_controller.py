from internal.domain.author.author_service import AuthorService
from internal.domain.author.author_payload import ListPayload
from internal.domain.book.book_service import BookService
from transport.http.response.response import Response
from transport.http.params.params import Params
from flask import request
from werkzeug.exceptions import NotFound
from dateutil import parser
from database.database import transaction

class AuthorController:
    @staticmethod
    def create():
        try:
            with transaction() as db:
                request_body = request.json
                AuthorService.create(db, request_body)
                return Response.handleResponse(None)
        
        except Exception as e:
            return Response.handleErr(e, None)

    @staticmethod
    def list():
        try:
            with transaction() as db:
                filter_name = request.args.get('name', None)
                start_birth_date_str = request.args.get('start_birth_date', None)
                end_birth_date_str = request.args.get('end_birth_date', None)
                start_birth_date = parser.isoparse(start_birth_date_str) if start_birth_date_str else None
                end_birth_date = parser.isoparse(end_birth_date_str) if end_birth_date_str else None

                pagination = Params.handlePagination(request)
                authors = AuthorService.list(db, ListPayload(
                    name=filter_name,
                    start_birth_date=start_birth_date,
                    end_birth_date=end_birth_date,
                    page=pagination['page'],
                    limit=pagination['limit']
                ))
                res = [
                    {
                        "id": author.id,
                        "name": author.name,
                        "bio": author.bio,
                        "birth_date": author.birth_date
                    } 
                    for author in authors
                ]
                return Response.handleResponse(res)
        
        except Exception as e:
            return Response.handleErr(e, None)
    
    @staticmethod
    def list_book_by_author_id(author_id):
        with transaction() as db:
            books = BookService.list_by_author_id(db, author_id)
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
    def find_by_id(author_id):
        try:
            with transaction() as db:
                res = AuthorService.find_by_id(db, author_id)
                return {
                        "id": res.id,
                        "name": res.name,
                        "bio": res.bio,
                        "birth_date": res.birth_date
                    } 

        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "author not found")
            
            return Response.handleErr(e, None)
        
    @staticmethod
    def update(author_id):
        try:
            with transaction() as db:
                request_body = request.json
                res = AuthorService.update(db, author_id, request_body)
                return {
                    "id": res.id,
                    "name": res.name,
                    "bio": res.bio,
                    "birth_date": res.birth_date
                } 

        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "author not found")
            
            return Response.handleErr(e, None)

        
    @staticmethod
    def delete(author_id):
        try:
            with transaction() as db:
                AuthorService.soft_delete(db, author_id)
                return Response.handleResponse(None)
        
        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "author not found")
            
            return Response.handleErr(e, None)