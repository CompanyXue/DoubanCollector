#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup 

from DoubanCollector.SaveToFile import *


def get_books_list():
    reqForbook = "This is douban book spider.\n"
    
    for i in range(0,250,25):
        url = "https://book.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        getImg(html,"bookImg",i)
        for table in soup.findAll('tr',class_= 'item'):
            print table
            reqForbook = reqForbook + str(table)+'\n\n'
            
    save2file(reqForbook, 'books.txt')       