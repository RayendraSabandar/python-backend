from flask import Blueprint, jsonify, request
from transport.http.controller.author_controller import AuthorController

author_bp_routes = Blueprint('author_bp_routes', __name__)

# Route to get all authors
@author_bp_routes.route('/', methods=['GET'])
def list():
    return AuthorController.list()