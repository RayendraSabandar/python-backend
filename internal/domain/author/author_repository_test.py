import pytest
from flask import abort
from internal.models.author_model import Author
from internal.domain.author.author_repository import AuthorRepository

@pytest.fixture
def mock_author():
    return Author(name="Test Author", bio="Test Bio", birth_date="2000-01-01")

@pytest.fixture
def mock_list_authors():
    authors = [
        Author(id=1, name="Author One", bio="Test Bio One", birth_date="1990-01-01"),
        Author(id=2, name="Author Two", bio="Test Bio Two", birth_date="1985-05-05"),
        Author(id=3, name="Author Three", bio="Test Bio Three", birth_date="1975-10-10"),
    ]
    return authors

@pytest.fixture
def mock_list_authors_empty_array():
    return []

def test_create(mocker, mock_author):
    db = mocker.Mock()
    AuthorRepository.create(db, mock_author)
    db.add.assert_called_once_with(mock_author)

def test_list(mocker, mock_list_authors):
    db = mocker.Mock()
    mock_payload = mocker.Mock(name="Author", start_birth_date=None, end_birth_date=None, page=1, limit=10)
    
    query_mock = mocker.Mock()
    db.query.return_value = query_mock
    query_mock.filter_by.return_value = query_mock
    query_mock.filter.return_value = query_mock
    query_mock.paginate.return_value = mocker.Mock(items=mock_list_authors)

    results = AuthorRepository.list(db, mock_payload)
    assert results == mock_list_authors
    query_mock.filter_by.assert_called_once_with(deleted_at=None)
    
def test_list_empty_array(mocker, mock_list_authors_empty_array):
    db = mocker.Mock()
    mock_payload = mocker.Mock(name="Author", start_birth_date=None, end_birth_date=None, page=1, limit=10)
    
    query_mock = mocker.Mock()
    db.query.return_value = query_mock
    query_mock.filter_by.return_value = query_mock
    query_mock.filter.return_value = query_mock
    query_mock.paginate.return_value = mocker.Mock(items=mock_list_authors_empty_array)

    results = AuthorRepository.list(db, mock_payload)
    assert results == mock_list_authors_empty_array
    query_mock.filter_by.assert_called_once_with(deleted_at=None)

def test_find_by_id_found(mocker, mock_author):
    db = mocker.Mock()
    db.query(Author).filter_by.return_value.first.return_value = mock_author
    author = AuthorRepository.find_by_id(db, 1)
    assert author == mock_author
    db.query(Author).filter_by.assert_called_once_with(deleted_at=None, id=1)

def test_find_by_id_not_found(mocker):
    db = mocker.Mock()
    db.query(Author).filter_by.return_value.first.return_value = None
    with pytest.raises(Exception, match="404"):
        AuthorRepository.find_by_id(db, 1)

def test_update(mocker, mock_author):
    db = mocker.Mock()
    updated_author = AuthorRepository.update(db, mock_author)
    assert updated_author == mock_author