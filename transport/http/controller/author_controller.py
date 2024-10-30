from internal.domain.author.author_service import AuthorService
from transport.http.response.response import Response
from flask import request

class AuthorController:
    @staticmethod
    def create():
        try:
            request_body = request.json
            AuthorService.create(request_body)
        
        except Exception as e:
            return Response.handleErr(e)

    @staticmethod
    def list():
        authors = AuthorService.list()
        authors_list = [
            {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "birth_date": author.birth_date
            } 
            for author in authors
        ]
        return Response.handleResponse(authors_list)