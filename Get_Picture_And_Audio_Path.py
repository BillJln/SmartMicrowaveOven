#! /usr/bin/python
# -*- coding: utf-8 -*-

import os


def get_file_name(path, suffix):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    file_list = os.listdir(path)
    # print f_list
    for file in file_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(file)[1] == suffix:
            return file

# if __name__ == '__main__':
#     path = 'D:/PycharmProject/app/static/images'
#     suffix='.jpg'
#     get_file_name(path,suffix)
