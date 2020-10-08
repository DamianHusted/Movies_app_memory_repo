import csv
import os
from datetime import date, datetime
from typing import List

from werkzeug.security import generate_password_hash

from app.domainmodel import actor, director, genre, movie, review, user, watchlist

