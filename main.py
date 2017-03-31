# -*- coding:utf-8 -*-

'''
main source file for this spider program.
'''

import sys

from book import get_books_list
from movie import get_movie_list
from music import get_music_list


def main():
    get_books_list()
    get_music_list()
    get_movie_list()

    sys.exit()
