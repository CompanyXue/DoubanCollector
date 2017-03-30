#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
from urllib2 import urlopen

from bs4 import BeautifulSoup

from DoubanCollector.main import save2file


def get_movie_one(movie):
    result = []
    soup_all = BeautifulSoup(str(movie))
    title = soup_all.find_all('div', class_='hd')
    soup_title = BeautifulSoup(str(title[0]))
    for line in soup_title.stripped_strings:  # 对获取到的<a>里的内容进行提取
        print line
        result.append(line)
    num = soup_all.find_all('span', class_='title')
    print num[0].contents[0]
    
    info = soup_all.find_all('div', class_='bd')
    soup_info = BeautifulSoup(str(info[0]))
    for line in soup_info.stripped_strings:  # 对获取到的<a>里的内容进行提取
        print line


def get_movie_list():
    reqFormovie = "This is douban movie spider.\n"
    for i in range(0,250,25):
        url = "https://movie.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        for li in soup.findAll('div', class_='info'):
            print li
            get_movie_one(li)
            reqFormovie = reqFormovie + str(li)+'\n\n'
            
    save2file(reqFormovie, "movies.txt")       
