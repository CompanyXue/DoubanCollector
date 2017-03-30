#-*- coding:utf-8 -*-

'''
main source file for this spider program.
'''

import sys
import string
from urllib2 import urlopen
from bs4 import BeautifulSoup 

from movies import get_movie_list

def save2file(stry,filename):
    try:  
        f = open(filename,'w+')
        f.write(stry.encode("utf8"))
    except IOError as err:
        print 'File error :' + str(err)
    finally: 
        f.close()
    pass

def main():
    #This is request content for writing into file.
    reqForbook = "This is douban book spider.\n"
    reqFormusic = "This is douban music spider.\n"
    print("This is douban spider.\n")
    
    for i in range(0,250,25):
        url = "https://book.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        for table in soup.findAll('table'):
            print table
            reqForbook = reqForbook + str(table)+'\n\n'
            
        id3 = string.replace(url,"book","music")
        html3 = urlopen(id3).read()
        soup2 = BeautifulSoup(html3)
        for table in soup2.findAll('table'):
            reqFormusic = reqFormusic + str(table) + '\n\n'

    save2file(reqForbook, "books.txt")   
    save2file(reqFormusic, "musics.txt")       
    get_movie_list()
    
    sys.exit()        
    
