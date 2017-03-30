#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
from urllib2 import urlopen

from bs4 import BeautifulSoup

from DoubanCollector.SaveToFile import save2file


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
    
    result_str = ""
    info = soup_all.find_all('div', class_='bd')
    soup_info = BeautifulSoup(str(info[0]))
    for line in soup_info.stripped_strings:  # 对获取到的<a>里的内容进行提取
        print line
        result_str = result_str + line
    result.append(result_str)
    return result  #返回获取到的结果


def get_movie_list():
    reqFormovie = "This is douban movie spider.\n"
    
    for i in range(0,250,25):
        url = "https://movie.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        for li in soup.findAll('div', class_='info'):
            result = get_movie_one(li)
#             for i in range(4):
#                 print i,result[i]
                    
            reqFormovie = reqFormovie + '电影名：'+str(result[0])+'别名：'+str(result[1])+'播放状态：'+str(result[2]) +'介绍：'+str(result[3])+'\n\n'
            
    save2file(reqFormovie, 'movies.txt')       
    #写入文件之后会显示为全部u编码--不正常

