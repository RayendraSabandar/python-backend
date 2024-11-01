import pytest
from datetime import datetime
from internal.domain.book.book_service import BookService
from internal.models.book_model import Book
from internal.domain.book.book_repository import BookRepository

# Sample request bodies for testing
@pytest.fixture
def mock_request_body():
    return {
        'title': 'Test Book',
        'description': 'Test Description',
        'publish_date': '2000-01-01',
        'author_id': 1
    }

@pytest.fixture
def mock_book():
    return Book(id=1, title="Test Book", description="Test Description", author_id=1, publish_date="2000-01-01")

@pytest.fixture
def mock_payload(mocker):
    return mocker.Mock(title="Book", page=1, limit=10)

def test_create(mocker, mock_request_body):
    db = mocker.Mock()
    mocker.patch.object(BookRepository, 'create', return_value=None)

    BookService.create(db, mock_request_body)
    
    BookRepository.create.assert_called_once()
    BookRepository.create.assert_called_once_with(db, mocker.ANY)

def test_list(mocker, mock_payload):
    db = mocker.Mock()
    mock_books = [Book(id=1, title="Book One", description="Description One", publish_date="1990-01-01")]
    mocker.patch.object(BookRepository, 'list', return_value=mock_books)

    result = BookService.list(db, mock_payload)
    
    assert result == mock_books
    BookRepository.list.assert_called_once_with(db, mock_payload)

def test_find_by_id(mocker, mock_book):
    db = mocker.Mock()
    mocker.patch.object(BookRepository, 'find_by_id', return_value=mock_book)

    result = BookService.find_by_id(db, 1)

    assert result == mock_book
    BookRepository.find_by_id.assert_called_once_with(db, 1)

def test_update(mocker, mock_request_body, mock_book):
    db = mocker.Mock()
    mocker.patch.object(BookRepository, 'find_by_id', return_value=mock_book)
    mocker.patch.object(BookRepository, 'update', return_value=None)

    result = BookService.update(db, 1, mock_request_body)

    assert result == mock_book
    assert mock_book.title == mock_request_body['title']
    assert mock_book.description == mock_request_body['description']
    assert mock_book.publish_date == mock_request_body['publish_date']
    BookRepository.find_by_id.assert_called_once_with(db, 1)
    BookRepository.update.assert_called_once_with(db, mock_book)

def test_soft_delete(mocker, mock_book):
    db = mocker.Mock()
    mocker.patch.object(BookRepository, 'find_by_id', return_value=mock_book)
    mocker.patch.object(BookRepository, 'update', return_value=None)

    result = BookService.soft_delete(db, 1)

    assert result == mock_book
    assert mock_book.deleted_at is not None
    BookRepository.find_by_id.assert_called_once_with(db, 1)
    BookRepository.update.assert_called_once_with(db, mock_book)