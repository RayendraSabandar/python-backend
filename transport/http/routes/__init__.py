from .author_routes import author_bp_routes

def register_blueprints(app, url_prefix):
    # Register each blueprint with the desired URL prefix
    app.register_blueprint(author_bp_routes, url_prefix=f"{url_prefix}/authors")
