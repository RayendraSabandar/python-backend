from flask import Blueprint
from transport.http.controller.book_controller import BookController

book_bp_routes = Blueprint('book_bp_routes', __name__)

@book_bp_routes.route('/', methods=['GET'])
def list():
    return BookController.list()