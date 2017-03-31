# -*- coding:utf-8 -*-

'''
Created on 2017年3月30日

@author: stone
'''

import re
import urllib
import os

def save2file(stry, filename):
    '''
        这个方法是用于保存文件的
    Input
        @param stry: 待寫入文件
        @param filename: 文件名
    Output：
        one file
    '''
    try:
        f = open(filename, 'w+')
        f.write(stry.encode("utf-8"))
    except IOError as err:
        print 'File error :' + str(err)
    finally:
        f.close()
    pass


def getImg(html, path, count):
    '''
        这个方法是用于下载图片的，实验成功
    '''
    # 自动创建目录
    if not os.path.exists(path):
        os.makedirs(path)

    reg = r'img src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,path+'/%s.jpg' % count)
        print count,imgurl
        count += 1
        
def set_image_download(path):   

    if not os.path.exists(path):
        os.makedirs(path)
    
    fname =path+'/downloaded'
  
    if not os.path.exists(fname):
        try:  
            des = open(fname, 'w+')

        except IOError as err:
            print 'File error :' + str(err)
        finally: 
            des.close()
