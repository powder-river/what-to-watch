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
def user_ratings():
    user_id = input("Enter a user id to find that user's reviews\n")
    user = User(user_id)
    review_list = user.user_rating_list()
    print("Here all all movie reviews of user id: {}".format(user_id))
    user_reviews = user.movie_ratings(review_list)
    # print("Here are all movies reviewd by user {}: {}".format(user_id, user_reviews))


def movie_ratings():

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
    """)

    if choice == '1':
        average_rating()
    elif choice == '2':
        user_ratings()
    else:
        print("Goodbye")



main()
