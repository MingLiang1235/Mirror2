#!/usr/bin/python3
# -*- coding:utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  test_weather.py   v.1.1
#   Perporse:  Test weather module which get weather data from hefeng
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################
#from weather import getWeatherResponse, getWeatherContent, getWeatherDictionary, getWeather
from weather import getWeather
import importlib
import sys
importlib.reload(sys)
""" import sys
reload(sys)
sys.setdefaultencoding('utf-8')
python2 use,python3 not use it."""
# r = getWeatherResponse()
# c = getWeatherContent(r)
# dic = getWeatherDictionary(c)
# print(getWeather())
print(getWeather())