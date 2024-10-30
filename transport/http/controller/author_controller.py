from internal.domain.author.author_service import AuthorService
from transport.http.response.response import Response

class AuthorController:
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