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
    title_str = ""
    soup_all = BeautifulSoup(str(movie))
    title = soup_all.find_all('a')
    soup_title = BeautifulSoup(str(title[0]))
    for line in soup_title.stripped_strings:  
        print line
        title_str = title_str + line
    result.append(title_str)
    #num = soup_all.find_all('span', class_='title')
    #print 'title: ',num[0].contents[0]
    
    info = soup_all.find_all('div', class_='bd')
    soup_info = BeautifulSoup(str(info[0]))
    for line in soup_info.stripped_strings:  #提取list詳細信息
        print line
        result.append(line)
        
    return result  #返回获取到的结果


def get_movie_list():
    reqFormovie = "This is douban movie spider.\n"
    
    for i in range(0,250,25):
        url = "https://movie.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        
        for li in soup.findAll('div', class_='info'):
            result = get_movie_one(li)
            # 解決不同列表不同大小的問題-- 統一截取為6項信息
            if len(result)<6:
                result.append(" no conclusion!")    
                
            reqFormovie = reqFormovie + '电影名：'+str(result[0])+'\t'+str(result[1])+'\t'+str(result[2]) +\
               '\t 评分：'+ str(result[3])+'\t'+str(result[4])+'\t 总结：'+str(result[5])+'\n\n'
            
    save2file(reqFormovie, 'movies.csv')       

