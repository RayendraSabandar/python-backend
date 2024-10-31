# app/transaction.py
from flask import g
from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager

db = SQLAlchemy()

@contextmanager
def transaction():
    session = db.session
    session.begin()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.remove()

def get_db():
    if 'db' not in g:
        g.db = db.session
    return g.db