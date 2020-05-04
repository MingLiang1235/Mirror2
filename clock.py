#!/usr/bin/python3
#-*- encoding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  clock.py 
#   Perporse:  Get current time and send it to main window
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################

import time
def getTime():
    return time.strftime("%Y %H:%M:%S %b %d %a", time.localtime())
    # my_time = time.localtime(time.time())

    # if my_time[3] < 10:
    #     hour = '0' + str(my_time[3])
    # else:
    #     hour = str(my_time[3])
    # if my_time[4] < 10:
    #     min = '0' + str(my_time[4])
    # else:
    #     min = str(my_time[4])
    # if my_time[5] < 10:
    #     second = '0' + str(my_time[5])
    # else:
    #     second = str(my_time[5])

    # return hour,min,second
