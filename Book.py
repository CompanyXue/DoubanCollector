#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''

import string
from urllib2 import urlopen
from bs4 import BeautifulSoup 

from DoubanCollector.SaveToFile import *


def get_book_one(book):
    result = []
    title_str = ""
    soup_all = BeautifulSoup(str(book))
    title = soup_all.find_all('div',class_='pl2')
    soup_title = BeautifulSoup(str(title[0]))
    for line in soup_title.stripped_strings:  
        print line
        title_str = title_str + line +'  '
    result.append(title_str)
    #result.append(title_str)
    
    info = soup_all.find_all('p', class_='pl')
    soup_info = BeautifulSoup(str(info[0]))
    for line in soup_info.stripped_strings:  #提取list詳細信息
        print line
        result.append(line)
    
    star = soup_all.find_all('span',class_="rating_nums") # 評分：星
    star_info = BeautifulSoup(str(star[0]))
    star = star_info.get_text()
    result.append(star)
    
    assessment = soup_all.find_all('span',class_="pl") # 评价 
    temp = BeautifulSoup(str(assessment[0]))
    asses = str(temp.get_text())
    # TODO 去除换行和空格
    string.strip(asses)
#     asses.replace('\r\n', 'A')
    result.append(asses)
    
    summary = soup_all.find_all('span',class_="inq") # summary 总结
    print "sum :",summary
    if summary!=[]:
        temp = BeautifulSoup(str(summary[0]))
        summer = temp.get_text()    
        result.append(summer)
    else :
        result.append("no conclusion!")
    
    return result

def get_books_list():
    reqForbook = "This is douban book spider.\n"
    
    for i in range(0,250,25):
        url = "https://book.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        getImg(html,"bookImg",i)
        for table in soup.findAll('tr',class_= 'item'):
            result = get_book_one(table)
            for id in range(5):
                print id , result[id]  
                   
            reqForbook = reqForbook + '书名：'+str(result[0])+'\t介绍：'+str(result[1])+'\t评分:'+\
                str(result[2])+str(result[3])+'\t总结: '+str(result[4])+'\n\n'
            
    save2file(reqForbook, 'books.txt')       