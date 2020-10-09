import csv
import os
from datetime import date, datetime
from typing import List

from werkzeug.security import generate_password_hash

from app.adaptors.repository.repository import AbstractRepository, RepositoryException
from app.domainmodel.actor import Actor
from app.domainmodel.director import Director
from app.domainmodel.genre import Genre
from app.domainmodel.review import Review
from app.domainmodel.movie import Movie
from app.domainmodel.user import User
from app.domainmodel.watchlist import Watchlist


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__dataset_of_users = list()
        self.__dataset_of_movies = list()
        self.__dataset_of_directors = set()
        self.__dataset_of_actors = set()
        self.__dataset_of_genres = set()
        self.__dataset_of_reviews = list()
        self.__dataset_of_watchlists = list()
        self.__ranklist = list()

    def add_user(self, user: User):
        if user not in self.__dataset_of_users:
            self.__dataset_of_users.append(user)
        else:
            print("User not added")
            return "User not added!"

    def get_user(self, username) -> User:
        return next((user for user in self.__dataset_of_users if user.username == username), None)

    def add_movie(self, movie: Movie):
        if movie not in self.__dataset_of_movies:
            self.__dataset_of_movies.append(movie)
        else:
            print("Movie not added")
            return "Movie not added"

    def get_movie(self, movie) -> Movie:
        return next((movie for movie in self.__dataset_of_movies if movie.movie_name == movie), None)

    def add_director(self, director: Director):
        if director not in self.__dataset_of_directors:
            self.__dataset_of_directors.add(director)

    def get_director(self, director) -> Director:
        return next((director for director in self.__dataset_of_directors if director.director_full_name == director),
                    None)

    def add_actor(self, actor: Actor):
        if actor not in self.__dataset_of_actors:
            self.__dataset_of_actors.add(actor)
        else:
            print("Actor not added")
            return "Actor not added"

    def get_actor(self, actor) -> Actor:
        return next((actor for actor in self.__dataset_of_actors if actor.actor_namec == actor), None)

    def add_genre(self, genre: Genre):
        if genre not in self.__dataset_of_genres:
            self.__dataset_of_genres.add(genre)
        else:
            print("Genre not added")
            return "Genre not added"

    def get_genre(self, genre) -> Genre:
        return next((genre for genre in self.__dataset_of_genres if genre.genre_name == genre), None)

    def add_review(self, review: Review):
        if review not in self.__dataset_of_reviews:
            self.__dataset_of_reviews.append(review)
        else:
            print("Review not added")
            return "Review not added"

    def get_review(self, review) -> Review:
        return next((review for review in self.__dataset_of_reviews if review.review_text == review), None)

    def add_watchlists(self, watchlist: Watchlist):
        if watchlist not in self.__dataset_of_watchlists:
            self.__dataset_of_watchlists.append(watchlist)
        else:
            print("Watchlist not added")
            return "Watchlist not added"

    def get_watchlists(self, watchlist) -> Watchlist:
        return self.__dataset_of_watchlists

    def get_number_of_movies(self):
        return len(self.__dataset_of_movies)

    def get_number_of_directors(self):
        return len(self.__dataset_of_directors)

    def get_number_of_actors(self):
        return len(self.__dataset_of_movies)

    def get_number_of_genres(self):
        return len(self.__dataset_of_genres)

    def get_number_of_reviews(self):
        return len(self.__dataset_of_reviews)

    def get_number_of_watchlists(self):
        return len(self.__dataset_of_watchlists)



def read_and_load_movie_file(file_name: str, repo: MemoryRepository):
    # noinspection SpellCheckingInspection
    with open(file_name, mode='r', encoding='utf-8-sig') as movie_file:
        movie_file_reader = csv.DictReader(movie_file)
        index = 0
        for row in movie_file_reader:
            rank = row['Rank']
            title = row['Title']
            director = row['Director']
            actor = row['Actors']
            release_year = int(row['Year'])
            genre = row['Genre']

            genre_list = genre.split(",")
            genre_list = [Genre(item.strip()) for item in genre_list]

            for item in genre_list:
                if item not in repo.__dataset_of_genres:  # or len(self.__dataset_of_genres) == 0:
                    repo.add_genre(item)

            actor_list = actor.split(",")
            actor_list = [Actor(item.strip()) for item in actor_list]

            for item in actor_list:
                if item not in repo.__dataset_of_actors:  # or len(self.__dataset_of_actors) == 0:
                    repo.add_actor(item)

            movie_object = Movie(title, release_year)
            if movie_object not in repo.__dataset_of_movies:  # or len(self.__dataset_of_movies) == 0:
                repo.add_movie(movie_object)

            director_object = Director(director)
            if director_object not in repo.__dataset_of_directors:  # or len(self.__dataset_of_directors) == 0:
                repo.add_director(director_object)

            index += 1


def read_and_load_user_file(file_name: str, repo: MemoryRepository):
    with open(file_name, mode='r', encoding='utf-8-sig') as users_file:
        user_file_reader = csv.DictReader(users_file)
        index = 0
        for row in user_file_reader:
            username = row['Username']
            user_id = row['User ID']
            user_pass = row['Password']
            user_first_name = row['First Name']
            user_last_name = row['Last Name']
            user_age = int(row['Age'])
            user_email = row['Email']
            user_consent = bool(row['Consent'])

            user_object = User(username, user_pass,user_id, user_first_name, user_last_name, user_age, user_email, user_consent)
            if user_object not in repo.__dataset_of_users:
                repo.add_user(user_object)
            index += 1



