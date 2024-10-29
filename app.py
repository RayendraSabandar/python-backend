from flask import Flask
from dotenv import load_dotenv
from config import Config
from database.database import init_db
from flask_cors import CORS
from internal.models.author_model import Author
from internal.models.book_model import Book

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Initialize the database and migrations
init_db(app)