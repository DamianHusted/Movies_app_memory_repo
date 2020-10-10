from flask import Flask, render_template
import Movie_app.adaptors.repository.repository as repo
from Movie_app.adaptors.repository.memory_repository import MemoryRepository, read_and_load_user_file, read_and_load_movie_file


app = Flask(__name__)
from Movie_app.app import routing

user_file = "Movie_app/datafiles/users.csv"
movie_file = "Movie_app/datafiles/Data1000Movies.csv"

repo.repo_instance = MemoryRepository()
print(read_and_load_user_file(user_file, repo.repo_instance))
print(read_and_load_movie_file(movie_file, repo.repo_instance))


