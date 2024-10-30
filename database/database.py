from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy and Migrate instances
db = SQLAlchemy()
migrate = Migrate()

# add transaction
# create context to wrap the db
def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)