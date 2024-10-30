from internal.domain.author.author_service import AuthorService
from transport.http.response.response import Response
from flask import request
from werkzeug.exceptions import NotFound

class AuthorController:
    @staticmethod
    def create():
        try:
            request_body = request.json
            AuthorService.create(request_body)
            return Response.handleResponse(None)
        
        except Exception as e:
            return Response.handleErr(e, None)

    @staticmethod
    def list():
        authors = AuthorService.list()
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
    
    @staticmethod
    def find_by_id(author_id):
        try:
            res = AuthorService.find_by_id(author_id)
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
            request_body = request.json
            res = AuthorService.update(author_id, request_body)
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
            AuthorService.soft_delete(author_id)
            return Response.handleResponse(None)
        
        except Exception as e:
            if isinstance(e, NotFound):
                return Response.handleErr(e, "author not found")
            
            return Response.handleErr(e, None)