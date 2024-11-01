import pytest
from datetime import datetime
from internal.domain.author.author_service import AuthorService
from internal.models.author_model import Author
from internal.domain.author.author_repository import AuthorRepository

# Sample request bodies for testing
@pytest.fixture
def mock_request_body():
    return {
        'name': 'Test Author',
        'bio': 'Test Bio',
        'birth_date': '2000-01-01'
    }

@pytest.fixture
def mock_author():
    return Author(id=1, name="Test Author", bio="Test Bio", birth_date="2000-01-01")

@pytest.fixture
def mock_payload(mocker):
    return mocker.Mock(name="Author", page=1, limit=10)

def test_create(mocker, mock_request_body):
    db = mocker.Mock()
    mocker.patch.object(AuthorRepository, 'create', return_value=None)

    AuthorService.create(db, mock_request_body)
    
    AuthorRepository.create.assert_called_once()
    AuthorRepository.create.assert_called_once_with(db, mocker.ANY)

def test_list(mocker, mock_payload):
    db = mocker.Mock()
    mock_authors = [Author(id=1, name="Author One", bio="Bio One", birth_date="1990-01-01")]
    mocker.patch.object(AuthorRepository, 'list', return_value=mock_authors)

    result = AuthorService.list(db, mock_payload)
    
    assert result == mock_authors
    AuthorRepository.list.assert_called_once_with(db, mock_payload)

def test_find_by_id(mocker, mock_author):
    db = mocker.Mock()
    mocker.patch.object(AuthorRepository, 'find_by_id', return_value=mock_author)

    result = AuthorService.find_by_id(db, 1)

    assert result == mock_author
    AuthorRepository.find_by_id.assert_called_once_with(db, 1)

def test_update(mocker, mock_request_body, mock_author):
    db = mocker.Mock()
    mocker.patch.object(AuthorRepository, 'find_by_id', return_value=mock_author)
    mocker.patch.object(AuthorRepository, 'update', return_value=None)

    result = AuthorService.update(db, 1, mock_request_body)

    assert result == mock_author
    assert mock_author.name == mock_request_body['name']
    assert mock_author.bio == mock_request_body['bio']
    assert mock_author.birth_date == mock_request_body['birth_date']
    AuthorRepository.find_by_id.assert_called_once_with(db, 1)
    AuthorRepository.update.assert_called_once_with(db, mock_author)

def test_soft_delete(mocker, mock_author):
    db = mocker.Mock()
    mocker.patch.object(AuthorRepository, 'find_by_id', return_value=mock_author)
    mocker.patch.object(AuthorRepository, 'update', return_value=None)

    result = AuthorService.soft_delete(db, 1)

    assert result == mock_author
    assert mock_author.deleted_at is not None
    AuthorRepository.find_by_id.assert_called_once_with(db, 1)
    AuthorRepository.update.assert_called_once_with(db, mock_author)