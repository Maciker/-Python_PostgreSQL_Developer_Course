from movie import Movie
from user import User
"""ejemplo1
user = User("Iker")

my_movie = Movie("The Matrix", "Sci-Fi", True)

user.movies.append(my_movie)

print(user)
print(user.watched_movies())
"""
user = User("Iker")

user.add_movie("The Matrix", "sci-fi")
user.add_movie("The Lord of The Rings", "fantasy")
user.add_movie("Usual suspects", "thriller")

print(user.json())