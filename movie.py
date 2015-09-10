import csv

class Movie:
    def __init__(self,title):
        self.title = title

    def get_movie_id(self):
        f = open("movie_data/u.info.csv")
        csv_f = csv.reader(f)

        
        self.title






def the_nose(num):
    return num + 1
