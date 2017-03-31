# -*- coding:utf-8 -*-

'''
Created on 2017年3月30日

@author: stone
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup

from save_to_file import *


def get_music_one(music):
    result = []
    title_str = ""
    soup_all = BeautifulSoup(str(music))
    #直接得到歌曲名称---利用a标签的title或者内容
    title = soup_all.find_all('div',class_='pl2')
    soup_title = BeautifulSoup(str(title[0]))
    aa = soup_title.find_all('a')
#     print "title: ",soup_title,a
    soup_a = BeautifulSoup(str(aa))
    for line in soup_a.stripped_strings:  
        print line
        title_str = title_str +line
        
    result.append(title_str)
    
    info = soup_all.find_all('div', class_='star clearfix')
    soup_info = BeautifulSoup(str(info[0]))
    for line in soup_info.stripped_strings: # 評分：星
        print line
        result.append(line)
    
    return result


def get_music_list():
    req_for_music = "This is douban music spider.\n"

    for i in range(0, 250, 25):
        url = "https://music.douban.com/top250?start=" + str(i)
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        
        path = 'music_images'
         
        if not os.path.isfile(path+'/downloaded') :
            getImg(html,path,i)
    
        for table in soup.findAll('tr',class_= 'item'):

            result = get_music_one(table)
            for id in range(3):
                print id , result[id]  
#                    
            req_for_music = req_for_music + 'music name：'+str(result[0])+'\t评分:'+\
                str(result[1])+str(result[2])+'\n\n'
                
    set_image_download(path)
    save2file(req_for_music, 'musics.txt')     
    
    
