#with open("my_file.txt", "w") as f:
#    f.write("Hello Iker!")

from user import User
"""user.add_movie("The Lord of The Rings", "Fantasy")
user.add_movie("Chacal", "Thriller")

user.save_to_file()"""

user = User.load_from_file("Iker.txt")

print(user.movies)