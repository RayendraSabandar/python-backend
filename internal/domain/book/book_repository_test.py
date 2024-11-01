import pytest
from flask import abort
from internal.models.book_model import Book
from internal.domain.book.book_repository import BookRepository

@pytest.fixture
def mock_book():
    return Book(title="Test Book", description="Test description", author_id=1, publish_date="2000-01-01")

@pytest.fixture
def mock_list_books():
    books = [
        Book(id=1, title="Book One", description="Test description One", author_id=1, publish_date="1990-01-01"),
        Book(id=2, title="Book Two", description="Test description Two", author_id=2, publish_date="1985-05-05"),
        Book(id=3, title="Book Three", description="Test description Three", author_id=3, publish_date="1975-10-10"),
    ]
    return books

@pytest.fixture
def mock_list_books_empty_array():
    return []


def test_create(mocker, mock_book):
    db = mocker.Mock()
    BookRepository.create(db, mock_book)
    db.add.assert_called_once_with(mock_book)

def test_list(mocker, mock_list_books):
    db = mocker.Mock()
    mock_payload = mocker.Mock(title="Author", start_publish_date=None, end_publish_date=None, page=1, limit=10)
    
    query_mock = mocker.Mock()
    db.query.return_value = query_mock
    query_mock.filter_by.return_value = query_mock
    query_mock.filter.return_value = query_mock
    query_mock.paginate.return_value = mocker.Mock(items=mock_list_books)

    results = BookRepository.list(db, mock_payload)
    assert results == mock_list_books
    query_mock.filter_by.assert_called_once_with(deleted_at=None)

def test_list_empty_array(mocker, mock_list_books_empty_array):
    db = mocker.Mock()
    mock_payload = mocker.Mock(title="Author", start_publish_date=None, end_publish_date=None, page=1, limit=10)
    
    query_mock = mocker.Mock()
    db.query.return_value = query_mock
    query_mock.filter_by.return_value = query_mock
    query_mock.filter.return_value = query_mock
    query_mock.paginate.return_value = mocker.Mock(items=mock_list_books_empty_array)

    results = BookRepository.list(db, mock_payload)
    assert results == mock_list_books_empty_array
    query_mock.filter_by.assert_called_once_with(deleted_at=None)

def test_find_by_id_found(mocker, mock_book):
    db = mocker.Mock()
    db.query(Book).filter_by.return_value.first.return_value = mock_book
    book = BookRepository.find_by_id(db, 1)
    assert book == mock_book
    db.query(Book).filter_by.assert_called_once_with(deleted_at=None, id=1)

def test_find_by_id_not_found(mocker):
    db = mocker.Mock()
    db.query(Book).filter_by.return_value.first.return_value = None
    with pytest.raises(Exception, match="404"):
        BookRepository.find_by_id(db, 1)

def test_update(mocker, mock_book):
    db = mocker.Mock()
    updated_book = BookRepository.update(db, mock_book)
    assert updated_book == mock_book