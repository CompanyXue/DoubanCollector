#-*- coding:utf-8 -*-

'''
main source file for this spider program.
'''

import sys

from DoubanCollector.Book import get_books_list
from DoubanCollector.Movie import get_movie_list
from DoubanCollector.Music import get_music_list


def main():
    
    print("This is douban spider.\n")
    
    get_books_list()
    get_music_list()    
    get_movie_list()
    
    sys.exit()        
    
