from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    __user_name: str
    __password: str
    __watched_movies: list
    __reviews: list
    __time_spent_watching_movies_minutes: int
    __complete_viewing_history: dict

    def __init__(self, user_name: str, password: str):
        if user_name is None or not isinstance(user_name, str) or user_name == "" or user_name == "\n":
            self.__user_name = None
        else:
            user_name = user_name.strip()
            self.__user_name = user_name.lower()
        if password is None or not isinstance(password, str) or password == "\n" or password == "":
            self.__password = None
        else:
            self.__password = password
        self.__complete_viewing_history = {"Complete history": [], "Total viewing time": 0, "Unique movies viewed": [],
                                           "Reviews": []}
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    # @property
    # def user_name(self):
    #     return self.__user_name

    # @user_name.setter
    # def user_name(self, new_user_name):
    #     if new_user_name is not None and isinstance(new_user_name,
    #                                                 str) and new_user_name != "" and new_user_name != "\n":
    #         self.__user_name = new_user_name

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, new_user_name):
        if new_user_name is not None and isinstance(new_user_name,
                                                    str) and new_user_name != "" and new_user_name != "\n":
            self.__user_name = new_user_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if new_password is not None and isinstance(new_password, str) and new_password != "\n" and new_password != "":
            self.__password = new_password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, new_watched_movies):
        if isinstance(new_watched_movies, list):
            self.__watched_movies = new_watched_movies
            self.__complete_viewing_history["Unique movies viewed"] = new_watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, new_review_list):
        if isinstance(new_review_list, list):
            self.__reviews = new_review_list

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, replacement_time):
        if replacement_time >= 0:
            self.__time_spent_watching_movies_minutes = replacement_time

    @property
    def complete_viewing_history(self):
        return self.__complete_viewing_history

    @complete_viewing_history.setter
    def complete_viewing_history(self, new_viewing_history):
        if new_viewing_history is not None and isinstance(new_viewing_history, dict):
            self.__complete_viewing_history = new_viewing_history

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other_user):
        if self.__user_name == other_user.__user_name:
            return True
        else:
            return False

    def __lt__(self, other_user):
        return self.user_name < other_user.__user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie: Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__complete_viewing_history["Complete history"].append(movie)
            self.__complete_viewing_history["Total viewing time"] += self.__time_spent_watching_movies_minutes
            self.__complete_viewing_history["Unique movies viewed"].append(movie)
        else:
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__complete_viewing_history["Complete history"].append(movie)
            self.__complete_viewing_history["Total viewing time"] += self.__time_spent_watching_movies_minutes
            self.__complete_viewing_history["Unique movies viewed"].append(movie)

    def add_review(self, review_to_add):
        if review_to_add not in self.__reviews:
            self.__reviews.append(review_to_add)
            self.__complete_viewing_history["Reviews"].append(review_to_add)

            # # for added_password policy consider the following: # #

            # if len(password) < 8:
            #     print("Password must be at least 8 characters long")
            #     pass
            # non_alphanumeric_characters = 0
            # uppercase_characters = 0
            # lowercase_characters = 0
            # digits = 0
            # for index in range(len(password)):
            #     if password[index].isnumeric():
            #         digits += 1
            #         index += 1
            #     elif not password[index].isalnum():
            #         non_alphanumeric_characters += 1
            #         index += 1
            #     elif password[index].islower():
            #         lowercase_characters += 1
            #         index += 1
            #     elif password[index].isupper():
            #         uppercase_characters += 1
            #         index += 1
            #     else:
            #         index += 1
            # if non_alphanumeric_characters < 1 or uppercase_characters < 1 or lowercase_characters < 1 or digits < 1:
            #     print("Password must contain at least: 1 upper-case character, 1 lower-case character, "
            #           "1 digit and 1 non-alphamumeric character")
            #     pass
            # else:
            #     self.__password = password


#
# user0 = User("slowloris", "One Direction is da best musik")
# user1 = User("slowloris", "DEEEEEEEEEEJAAAAAAAAAAY KHAAAAALEED!")
# print(user0.__hash__())
# print(user1.__hash__())

user1 = User('Martin', 'pw12345')
user2 = User('Ian', 'pw67890')
user3 = User('Daniel', 'pw87465')
print(user1)
print(user2)
print(user3)

movie1 = Movie("Moana", 2016)
movie1.runtime_minutes = 60
review_text1 = "This movie was very enjoyable."
rating1 = 8
review1 = Review(movie1, review_text1, rating1)

movie2 = Movie("James Bond", 2016)
movie2.runtime_minutes = 80
review_text2 = "This movie was very tame."
rating2 = 5
review2 = Review(movie2, review_text2, rating2)

user1.watch_movie(movie1)
user1.add_review(review1)
print("User1 reviews", user1.reviews)
print("User1 movies", user1.watched_movies)
print("User1 time spent watching movies", user1.time_spent_watching_movies_minutes)
print("User1 complete viewing history", user1.complete_viewing_history)

user2.watch_movie(movie2)
user2.add_review(review2)
print("User2 reviews", user2.reviews)
print("User2 movies", user2.watched_movies)
print("User2 time spent watching movies", user2.time_spent_watching_movies_minutes)
print("User2 complete viewing history", user2.complete_viewing_history)
