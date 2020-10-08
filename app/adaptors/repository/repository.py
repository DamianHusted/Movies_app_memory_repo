import abc
from datetime import date
from app.domainmodel import *
from app.domainmodel.genre import Genre
from app.domainmodel.user import User
from app.domainmodel.movie import Movie

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        """:param user """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """:returns None if no user with the given username is found"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """Adds a movie to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie) -> Movie:
        """Returns Movie"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """Adds genre to repo"""
        raise NotImplementedError
        