import csv
import re
from movie import *
from user import *

"""
[]Find all ratings for a movie by id
[x]Find the average rating for a movie by id
[]Find the name of a movie by id
[x]Find all ratings for a user

"""
def title_to_id(title):
    title

def user_ratings():
    user_id = input("Enter a user id to find that user's reviews\n")
    user = User(user_id)
    review_list = user.user_rating_list()
    print("Here all all movie reviews of user id: {}".format(user_id))
    user.movie_ratings(review_list)
    # print("Here are all movies reviewd by user {}: {}".format(user_id, user_reviews))


def movie_ratings():
    movie_title = input("Enter Movie Title\n").lower()
    movie = Movie(movie_title)
    titles = movie.movie_titles()
    movie_id = movie.get_movie_id(titles)

    print("Getting Results For: {}".format(movie.get_movie_name(titles)))
    movie = Movie(movie_id)
    review_list = movie.user_rating_list()

    movie.movie_ratings(review_list, movie_id)


def average_rating():
    movie_id = input("Enter Movie ID\n")
    movie = Movie(movie_id)
    review_list = movie.user_rating_list()
    average = movie.average_review(review_list)
    print("The average review of your movie is {}/5 stars".format(average))



def main():
    choice = input("""
    Welcome to the Move Review Database(1998). What Would you like to do?

    [1]-- Find The Average Review of a Movie
    [2]-- Find All Reviews From a User
    [3]-- Find All Reviews For a Movie
    """)

    if choice == '1':
        average_rating()
    elif choice == '2':
        user_ratings()
    elif choice == '3':
        movie_ratings()
    else:
        print("Goodbye")



main()
