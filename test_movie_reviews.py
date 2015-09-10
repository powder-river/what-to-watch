from movie import *
from rating import *
from user import *
from nose.tools import raises

def test_nose_works():
    assert the_nose(5) == 6


def test_movie_class():
    assert Movie
    assert Movie.get_movie_id == "T"



def test_user_class():
    bob = User(1)
    assert User
    assert bob.user_id == 2


def test_rating_class():
    assert Rating
