import os
from flask import Flask
from dotenv import load_dotenv
from config import Config
from database.database import db
from flask_cors import CORS
from transport.http.routes import register_blueprints
from internal.models.author_model import Author
from internal.models.book_model import Book
from flask import jsonify

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Initialize the database and migrations
db.init_app(app)

@app.teardown_appcontext
def teardown_db(exception):
    db.session.remove()

ROUTE_PREFIX = os.getenv('ROUTE_PREFIX')
PORT = os.getenv('PORT')

@app.get("/ping")
def ping():
    response={"message": "pong"}
    return jsonify(response)

register_blueprints(app, url_prefix=ROUTE_PREFIX)

if __name__=="__main__":
    app.run(port=PORT, debug=True)