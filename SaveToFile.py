#-*- coding:utf-8 -*-
'''
Created on 2017年3月30日

@author: stone
'''
def save2file(stry,filename):
    try:  
        f = open(filename,'w+')
        f.write(stry.encode("utf-8"))
    except IOError as err:
        print 'File error :' + str(err)
    finally: 
        f.close()
    pass