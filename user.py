import re
import csv

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    """ need to have a dictonry of users
        users = {
            user_id:stuff,
            user_id:stuff,
            user_id:stuff,
        }
        well, maybe......
    """
    def user_rating_list(self):
        array = []
        with open("movie_data/u.data.csv") as w:
            movie_data = w.readlines()
        for i in movie_data:
            i = re.sub(r'[\\tn]', " ", i)
            i = i.split()
            array.append(i)
        return array


    def movie_ratings(self, user_ratings):
        array = []
        for i in user_ratings:
            if i[0] == self.user_id:
                print("Movie:{},  Rating:{}".format(i[1], i[2]))
