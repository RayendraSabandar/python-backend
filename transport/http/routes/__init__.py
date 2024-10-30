from .author_routes import author_bp_routes
from .book_routes import book_bp_routes

def register_blueprints(app, url_prefix):
    app.register_blueprint(author_bp_routes, url_prefix=f"{url_prefix}/authors")
    app.register_blueprint(book_bp_routes, url_prefix=f"{url_prefix}/books")
