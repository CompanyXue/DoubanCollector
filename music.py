# -*- coding:utf-8 -*-

'''
Created on 2017年3月30日

@author: stone
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup

from save_to_file import save2file, getImg


def get_music_list():
    req_for_music = "This is douban music spider.\n"

    for i in range(0, 250, 25):
        url = "https://music.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        getImg(html, "musicImg", i)
        for table in soup.findAll('tr', class_='item'):
            req_for_music = req_for_music + str(table) + '\n\n'

    save2file(req_for_music, 'musics.txt')
