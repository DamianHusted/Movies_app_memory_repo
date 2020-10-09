from flask import Flask
from app import routing
from app import admin_routing
import app.adaptors.repository.repository as repo
from app.adaptors.repository.memory_repository import MemoryRepository, read_and_load_user_file, read_and_load_movie_file

app = Flask(__name__)


user_file = "app/datafiles/users.csv"
movie_file = "app/datafiles/Data1000Movies.csv"

repo.repo_instance = MemoryRepository()
read_and_load_user_file(user_file, repo.repo_instance)
read_and_load_movie_file(movie_file, repo.repo_instance)

