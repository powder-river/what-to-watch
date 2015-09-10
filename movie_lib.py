import csv
import re
from movie import *
#================================================
# with open("movie_data/u.user.csv") as w:
#     word_dictionary = w.read()
#     word_dictionary = word_dictionary.split()
# print(word_dictionary)
# if "technician" in
# for i in word_dictionary:
#     if "technician" in i:
#         i = re.sub(r'\|'," ",i)
#         i = i.split()
#
#         print(i)
# ================================================
with open("movie_data/u.item.csv") as w:
    movie_info = w.read()
    movie_info = movie_info.split()



print(movie_info)
