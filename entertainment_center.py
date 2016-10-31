# Importing Movie class from media module
from media import Movie
# Importing fresh_tomatoes module
import fresh_tomatoes
# Initializing list variable
movie_objects = []

# Creating Movie object for all the movies in the favorite_movie_list.txt file
# and adding them in the list movie_objects
with open("favorite_movie_list.txt", "r") as favorite_movie_list:
    next(favorite_movie_list)
    for movie in favorite_movie_list:
        movie_details = movie.split(",")
        movie_object = Movie(movie_details[0], movie_details[1],
                             movie_details[2], movie_details[3],
                             movie_details[4])
        movie_objects.append(movie_object)

# Passing list of Movie objects to OOB fresh_tomatoes module fuction
# open_movie_page which in turn creates html page using these Movie objects
# and opens the html page in the browser
fresh_tomatoes.open_movies_page(movie_objects)
