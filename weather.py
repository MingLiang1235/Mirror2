#!/usr/bin/python3
# -*- coding:utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  weather.py   v.1.1 
#   Perporse:  Module which get weather data from hefeng
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################

import requests, sys
import json
import importlib
import sys
importlib.reload(sys)

# def getWeatherResponse(url):
#     response = requests.get(url)
#     #print("response:" + str(response))
#     #print("response.text:" + response.text)
#     return response
# def getWeatherContent(response):
#     #print("bytes:(type(response.content)):" + str(type(response.content)))
#     #print("response.content:" + str(response.content))
#     return response.content
# def getWeatherDictionary(content):
#     dict = json.loads(content)
#     print(str(dict))
#     return dict
####################################
# 直接打开气象url，并将结果转化成字典
####################################
def getWeatherDictionary(url):
    response = requests.get(url)
    content = response.content
    dict = json.loads(content)
    return dict

def getWeather():
    host_now = 'https://free-api.heweather.net/s6/weather/now?location=CN101010100&key=f376edb228bd4ae489fc065fb3f88d1c'  
    dict_now = getWeatherDictionary(host_now)
    host_forecast = 'https://free-api.heweather.net/s6/weather/forecast?location=CN101010100&key=f376edb228bd4ae489fc065fb3f88d1c'
    dict_forecast = getWeatherDictionary(host_forecast)
    #print(str(dict_now))
    #print(str(dict_forecast))
    three_day = []
    weather_data = {}
    tmp_max = None
    tmp_min = None
    if dict_forecast['HeWeather6'][0]['status'] == 'ok':
        ls_fore = dict_forecast['HeWeather6'][0]['daily_forecast']
        i = 0
        for fore_item in ls_fore:
            i+=1
            if i == 1:  # 第一天和now是同一天，所以略去
                tmp_max = fore_item['tmp_max']
                tmp_min = fore_item['tmp_min']
            else:
                if i == 2:
                    forecast_one_day = storeData(fore_item)
                    three_day.append(forecast_one_day)
                elif i == 3:
                    forecast_one_day = storeData(fore_item)
                    three_day.append(forecast_one_day)
                elif i == 4:  # 可获取3-10天，如果只获取3天，则这一项为空，len(three_day)=2
                    forecast_one_day = storeData(fore_item)
                    three_day.append(forecast_one_day)
    if dict_now['HeWeather6'][0]['status'] == 'ok':
        weather_data['city'] = dict_now['HeWeather6'][0]['basic']['location']  # 城市名（中文）
        #weather_data['date'] = dict_now['HeWeather6'][0]['update']['loc'][:10]  # 日期,不包括时间
        weather_data['date'] = dict_now['HeWeather6'][0]['update']['loc']  # 日期,包括时间
        weather_data['three_day'] = three_day
        tmp_now = dict_now['HeWeather6'][0]['now']['tmp']
        wind_dir_now = dict_now['HeWeather6'][0]['now']['wind_dir']
        wind_sc_now = dict_now['HeWeather6'][0]['now']['wind_sc'] + u'级'
        cond_txt_now = dict_now['HeWeather6'][0]['now']['cond_txt']
        now = {'cond_txt':cond_txt_now, 'tmp':tmp_now, 'tmp_min':tmp_min, 'tmp_max':tmp_max, 'wind_dir':wind_dir_now, 'wind_sc':wind_sc_now}
        weather_data['now'] = now
    return weather_data

def storeData(item):
    dict = {'cond_txt_d':item['cond_txt_d'], 
            'date':item['date'][5:],  # 日期，不包括年份
            'tmp_max':item['tmp_max'],
            'tmp_min':item['tmp_min'],
            'wind_dir':item['wind_dir'],  # 中文，“北风”
            'wind_sc':item['wind_sc'] + u'级'}
    return dict
    #host = 'https://free-api.heweather.com/v5/forecast?city=CN101120201&key=4f4aa9f984ad44c2b2fdd78280b31900'
#     host_now = 'https://free-api.heweather.com/v5/now?city=CN101120201&key=4f4aa9f984ad44c2b2fdd78280b31900'
#     # 下载数据
#     content1 = loadData(host)
#     content2 = loadData(host_now)
#     #print(content_data)
#     dic_data = json.loads(content1)['HeWeather5'][0]['daily_forecast']
#     realtime_data = json.loads(content2)['HeWeather5'][0]['now']['tmp']
#     i = 0
#     threeday_data = []
#     for key in dic_data:
#         #print(key)
#         i += 1
#         if(i==1):
#            today_data = storeData(key)
#            threeday_data.append(today_data)
#         elif(i==2):
#             tmr_data = storeData(key)
#             threeday_data.append(tmr_data)
#         elif(i==3):
#             dat_data = storeData(key)
#             threeday_data.append(dat_data)
#     threeday_data.append(realtime_data)
#     #print(threeday_data)
#     return threeday_data
# def loadData(url):
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     content_data = response.read().decode('utf-8')
#     return content_data
# def storeData(key):
#     alldata = []
#     alldata.append(key['cond']['txt_d'])
#     alldata.append(key['date'])
#     alldata.append(key['hum'])
#     alldata.append(key['tmp']['max'])
#     alldata.append(key['tmp']['min'])
#     alldata.append(key['wind']['dir'])
#     alldata.append(key['wind']['sc'])
#     return alldata

#getWeather()

'''
    # 解析JSON
    
    需要的数据：
    city\date\week\weather\temp\temphigh\templow\humidity\winddirect\windpower
    
    weather_data = {}
    dic_data = json.loads(content_data)['result']
    for key in dic_data:
        if (key == "city"):
            weather_data['city'] = dic_data['city']
        elif(key == "date"):
            weather_data['date'] = dic_data['date']
        elif (key == "week"):
            weather_data['week'] = dic_data['week']
        elif (key == "weather"):
            weather_data['weather'] = dic_data['weather']
        elif (key == "temp"):
            weather_data['temp'] = dic_data['temp']
        elif (key == "humidity"):
            weather_data['humidity'] = dic_data['humidity']
        elif (key == "winddirect"):
            weather_data['winddirect'] = dic_data['winddirect']
        elif (key == "windpower"):
            weather_data['windpower'] = dic_data['windpower']

    return weather_data
    '''
