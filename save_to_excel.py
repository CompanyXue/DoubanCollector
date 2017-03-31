# -*- coding:utf-8 -*-

'''
Created on 2017-03-31

@author: Maxwell Lee
'''

from openpyxl import Workbook


def print_movie_list_excel(movie_list):
    wb = Workbook()
    ws = wb.active
    ws.title = '电影Top250'.decode()
    ws.append(['序号', '电影名', '介绍', '类型', '评分', '评价人数', '总结'])

    count = 1
    for movie in movie_list:
        ws.append([count] + movie)
        count += 1

    wb.save('movie_top250.xlsx')
