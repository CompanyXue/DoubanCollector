#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
from urllib2 import urlopen
from bs4 import BeautifulSoup

from DoubanCollector.SaveToFile import save2file, getImg


def get_music_one(music):
    result = []
    title_str = ""
    soup_all = BeautifulSoup(str(music))
    title = soup_all.find_all('div',class_='pl2')
    
    
    return result
    pass


def get_music_list():
    reqFormusic = "This is douban music spider.\n"
    
    for i in range(0,250,25):
        url = "https://music.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        getImg(html,"musicImg",i)
        for table in soup.findAll('tr',class_= 'item'):
            result = get_music_one(table)
            for id in range(5):
                print id , result[id]  
                   
            reqFormusic = reqFormusic + 'music name：'+str(result[0])+'\tintroduce ：'+str(result[1])+'\t评分:'+\
                str(result[2])+str(result[3])+'\tsummary: '+str(result[4])+'\n\n'
                
    save2file(reqFormusic, 'musics.txt')     
    
    