import csv
import re
from movie import *
#================================================
with open("movie_data/u.user.csv") as w:
      word_dictionary = w.read()
      word_dictionary = word_dictionary.split()


# for i in word_dictionary:
#   if "technician" in i:
#       i = re.sub(r'\|'," ",i)
#       i = i.split()
#       print(i)
# print(word_dictionary)
# ================================================
with open("movie_data/u.data.csv") as w:
  movie_data = w.readlines()
  for i in movie_data:
    i = re.sub(r'[\\tn]', " ", i)
    i = i.split()
    print(i)



    # movie_data = movie_data.split()
