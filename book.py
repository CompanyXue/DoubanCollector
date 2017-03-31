# -*- coding:utf-8 -*-

'''
Created on 2017年3月30日

@author: stone
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup

from save_to_file import *


def get_books_list():
    req_for_book = ""

    for i in range(0, 250, 25):
        url = "https://book.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        getImg(html, "book_images", i)
        for table in soup.findAll('tr', class_='item'):
            print table
            req_for_book = req_for_book + str(table) + '\n\n'

    save2file(req_for_book, 'books.txt')
