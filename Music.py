#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
from urllib2 import urlopen
from bs4 import BeautifulSoup

from DoubanCollector.SaveToFile import save2file, getImg


def get_music_list():
    reqFormusic = "This is douban music spider.\n"
    
    for i in range(0,250,25):
        url = "https://music.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        getImg(html,"musicImg",i)
        for table in soup.findAll('tr',class_= 'item'):
            reqFormusic = reqFormusic + str(table) + '\n\n'
            
    save2file(reqFormusic, 'musics.txt')     
    
    