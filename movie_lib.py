import csv
import re
from movie import *
from user import *
#================================================
# with open("movie_data/u.user.csv") as w:
#       word_dictionary = w.read()
#       word_dictionary = word_dictionary.split()


# for i in word_dictionary:
#   if "technician" in i:
#       i = re.sub(r'\|'," ",i)
#       i = i.split()
#       print(i)
# print(word_dictionary)
# =====================takes in move data===========================
# array = []
# with open("movie_data/u.data.csv") as w:
#     movie_data = w.readlines()
# for i in movie_data:
#     i = re.sub(r'[\\tn]', " ", i)
#     i = i.split()
#     array.append(i)
#
#
# for i in array:
#     if i[0] == '1':
#         print(i)
input_id = input("Enter a user Id\n")
a_user = User(input_id)
user_list = a_user.user_rating_list()
print(a_user.find_user_ratings(user_list))

    # movie_data = movie_data.split()
