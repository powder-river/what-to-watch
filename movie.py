import csv
import re

class Movie:
    def __init__(self,movie_id):
        self.movie_id = movie_id

    def user_rating_list(self):
        array = []
        with open("movie_data/u.data.csv") as w:
            movie_data = w.readlines()
        for i in movie_data:
            i = re.sub(r'[\\tn]', " ", i)
            i = i.split()
            array.append(i)
        return array

    def average_review(self,user_ratings):
        array = []
        sum_array = []
        for i in user_ratings:
            if i[1] == self.movie_id:
                array.append(i)
        for i in array:
            i = int(i[2])
            sum_array.append(i)
        average = sum(sum_array)/len(array)
        return round(average,1)


    def movie_ratings(self, database):
        for i in database:
            if i[]










def the_nose(num):
    return num + 1
