#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
import re
import urllib


def save2file(stry,filename):
    '''
        这个方法是用于保存文件的
    Input
        @param stry: 待寫入文件
        @param filename: 文件名
    Output：
        one file
    '''
    try:  
        f = open(filename,'w+')
        f.write(stry.encode("utf-8"))
    except IOError as err:
        print 'File error :' + str(err)
    finally: 
        f.close()
    pass

def getImg(html,path,count):
    '''
        这个方法是用于下载图片的，实验成功
    '''
    reg = r'img src="(.+?\.jpg)" width="64"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
   
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,path+'/%s.jpg' % count)
        print count,imgurl
        count += 1