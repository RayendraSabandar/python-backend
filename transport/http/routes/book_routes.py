from flask import Blueprint
from transport.http.controller.book_controller import BookController

book_bp_routes = Blueprint('book_bp_routes', __name__)

@book_bp_routes.route('/', methods=['POST'])
def create():
    return BookController.create()

@book_bp_routes.route('/', methods=['GET'])
def list():
    return BookController.list()

@book_bp_routes.route('/<int:book_id>', methods=['GET'])
def find_by_id(book_id):
    return BookController.find_by_id(book_id)

@book_bp_routes.route('/<int:book_id>', methods=['PATCH'])
def update(book_id):
    return BookController.update(book_id)

@book_bp_routes.route('/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    return BookController.delete(book_id)