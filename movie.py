import csv
import re

class Movie:
    def __init__(self,title):
        self.title = title


    def movie_titles(self):
        array = []
        film_titles = []
        with open('movie_data/u.item.csv', encoding='latin_1') as f:
            reader = csv.reader(f,delimiter='|')
            # reader = csv.DictReader(f, fieldnames=['title', 'movie_title', '', '', 'something_else'], delimiter='|')
            for row in reader:
                array.append([row[0],row[1]])

        for n in array:
            n[1] = re.sub(r'\(\d+\)', "", n[1])
            film_titles.append(n)
        return film_titles


    def get_movie_id(self, title_list):
        for n in title_list:
            if self.title in n[1].lower():
                return n[0]


    def get_movie_name(self,title_list):
        for n in title_list:
            if self.title in n[1].lower():
                return n[1]

    # def movie_id(self):
    #     with open('u.item', encoding='latin_1') as f:
    #         reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
    #     for row in reader:
    #         print(row)

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


    def movie_ratings(self, user_ratings, movie_id):

        for i in user_ratings:
            if i[1] == movie_id :
                print("User ID: {},  Rating: {}".format(i[0], i[2]))










def the_nose(num):
    return num + 1
