from flask import Blueprint
from transport.http.controller.author_controller import AuthorController

author_bp_routes = Blueprint('author_bp_routes', __name__)

@author_bp_routes.route('/', methods=['POST'])
def create():
    return AuthorController.create()

@author_bp_routes.route('/', methods=['GET'])
def list():
    return AuthorController.list()

@author_bp_routes.route('/<int:author_id>/books', methods=['GET'])
def list_book_by_author_id(author_id):
    return AuthorController.list_book_by_author_id(author_id)

@author_bp_routes.route('/<int:author_id>', methods=['GET'])
def find_by_id(author_id):
    return AuthorController.find_by_id(author_id)

@author_bp_routes.route('/<int:author_id>', methods=['PATCH'])
def update(author_id):
    return AuthorController.update(author_id)

@author_bp_routes.route('/<int:author_id>', methods=['DELETE'])
def delete(author_id):
    return AuthorController.delete(author_id)