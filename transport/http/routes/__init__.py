from .author_routes import author_bp_routes
from .book_routes import book_bp_routes
from flask import Flask

def register_blueprints(app: Flask, url_prefix):
    app.register_blueprint(author_bp_routes, url_prefix=f"{url_prefix}/authors")
    app.register_blueprint(book_bp_routes, url_prefix=f"{url_prefix}/books")
