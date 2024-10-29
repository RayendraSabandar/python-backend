from flask import jsonify, request
from internal.domain.author.author_service import AuthorService

class AuthorController:
    @staticmethod
    def list():
        authors = AuthorService.list()
        authors_list = [{"id": author.id, "name": author.name, "bio": author.bio, "birth_date": author.birth_date} for author in authors]
        return jsonify(authors_list), 200