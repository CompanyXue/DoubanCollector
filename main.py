# -*- coding:utf-8 -*-

'''
main source file for this spider program.
'''

import sys
import string
from urllib2 import urlopen
from bs4 import BeautifulSoup


def save2file(stry, filename):
    try:
        f = open(filename, 'w+')
        f.write(stry.encode("utf8"))
    except IOError as err:
        print 'File error :' + str(err)
    finally:
        f.close()
    pass


def main():
    # This is request content for writing into file.
    # reqForbook = "This is douban book spider.\n"
    reqForbook = ""
    reqFormovie = "This is douban movie spider.\n"
    reqFormusic = "This is douban music spider.\n"
    # print("This is douban spider.\n")
    try:
        urls = open('urls.txt', 'r+')
        for id in urls:
            html = urlopen(id).read()
            soup = BeautifulSoup(html, "html.parser")

            for table in soup.findAll('table'):
                #print table
                #title = table.find('a', {'title'})
                print table.children
                #reqForbook = reqForbook + str(table) + '\n\n'
                #reqForbook = reqForbook + str(title) + '\n\n'

            '''
            id2 = string.replace(id, "book", "movie")
            html2 = urlopen(id2).read()
            soup2 = BeautifulSoup(html2)
            for li in soup2.findAll('li'):
                print li
                reqFormovie = reqFormovie + str(li) + '\n\n'

            id3 = string.replace(id, "book", "music")
            html3 = urlopen(id3).read()
            soup2 = BeautifulSoup(html3)
            for table in soup2.findAll('table'):
                reqFormusic = reqFormusic + str(table) + '\n\n'
            '''
        save2file(reqForbook, "books")
        # save2file(reqFormovie, "movies")
        # save2file(reqFormusic, "musics")

        sys.exit()
    except Exception as e:
        print 'File error :' + str(e)
    finally:
        urls.close()
