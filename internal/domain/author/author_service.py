from .author_repository import AuthorRepository

class AuthorService:
    @staticmethod
    def list():
        return AuthorRepository.list()