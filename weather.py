#!/usr/bin/python3
# -*- coding:utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  weather.py   v.1.2 
#   Perporse:  Module which get weather data from hefeng
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################

import requests, sys
import json
from window_loop import getStringWithWindow
import importlib
import sys
import mmap
import time
import contextlib
import threading
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
#--------------------------------------------------
# 直接打开气象url，并将结果转化成字典
#--------------------------------------------------
def getWeatherDictionary(url):
    response = requests.get(url)
    content = response.content
    # print('content:',content)
    dict = None
    try:
        dict = json.loads(content)  # content内容是合法json，可以被loads直接解析。
    except Exception as err:
        print('??? In getWeatherDictionary:', repr(err), url[54:66])
    return dict
#--------------------------------------------------
# 打开本城的天气情况，包括预告
#--------------------------------------------------
def getWeather():
    #host_now = 'https://free-api.heweather.net/s6/weather/now?location=CN101011700&key=f376edb228bd4ae489fc065fb3f88d1c'  
    host_now = getFromJsonConfig("weather_now")
    dict_now = getWeatherDictionary(host_now)
    #host_forecast = 'https://free-api.heweather.net/s6/weather/forecast?location=CN101011700&key=f376edb228bd4ae489fc065fb3f88d1c'
    host_forecast = getFromJsonConfig("weather_forecast")
    dict_forecast = getWeatherDictionary(host_forecast)
    #print(str(dict_now))
    #print(str(dict_forecast))
    three_day = []
    weather_data = {}
    tmp_max = None
    tmp_min = None
    if dict_forecast:
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
    if dict_now:
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
#--------------------------------------------------
# 由主程序决定每几分钟循环一次，获取数据(从共享文件)
#--------------------------------------------------
def getWeather2():  
    #return '1234567890abcde'
    #return '三亚,多云,22℃ 秦皇岛,晴,7℃ 大连,多云,8℃ 青岛,多云,10℃'
    #text = '三亚,多云,22℃ 秦皇岛,晴,7℃ 大连,多云,8℃ 青岛,多云,10℃'
    with open('weather.dat', 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)) as m:
            text = m.read(1024)
            text = str(text, encoding='utf-8').replace('\x00', '')
    # count = len(text)
    return text
#--------------------------------------------------
# 获取config（json文件）中的某一配置项。
#--------------------------------------------------
def getFromJsonConfig(key):
    load_dict = None
    try:
        with open('config', 'r') as load_f:
            load_dict = json.load(load_f)
            #print(load_dict)
    except Exception as err:
        print('!!!!!',repr(err))
    if load_dict:
        try:
            return load_dict[key]
        except Exception as err:
            print('?????',repr(err))
            return None
    else:
        return None
#--------------------------------------------------
# 启动Weather2Serveer，每小时获取一次数据，并写入共享文件供getWeather2读出。
#--------------------------------------------------
def getStrFromWeatherDict(str_result, dict_now):
    str_result += dict_now['HeWeather6'][0]['basic']['location']  # 城市名（中文）    
    str_result += ','
    str_result += dict_now['HeWeather6'][0]['now']['cond_txt']  # 天气情况
    str_result += ','
    str_result += dict_now['HeWeather6'][0]['now']['tmp']  # 实时气温
    str_result += chr(0x2103)
    str_result += ' '
    return str_result
#--------------------------------------------------
# 启动Weather2Serveer，每分钟获取一次数据，并写入共享文件供getWeather2读出。
#--------------------------------------------------
def runWeather2Server():  
    with open('weather.dat', 'wb') as f:  # 用1024个\x00填充weather.dat
        fill = '\x00' * 1024
        fill = fill.encode(encoding = 'utf-8') # turns str to bytes
        f.write(fill)  # write bytes to file
        f.close()

        str_result = ''  # 供写入weather.dat的天气字符串
        urls = getFromJsonConfig('PaoMaDeng')
        if urls:
            # print('Weather2 urls:', urls)
            for url in urls:
                weather_data = {}
                dict_now = getWeatherDictionary(url)  # 直接打开和风气象，返回气象数据字典
                if dict_now:  # contents是合法json,而非‘503’
                    if dict_now['HeWeather6'][0]['status'] == 'ok':
                        str_result = getStrFromWeatherDict(str_result, dict_now)
                else:
                    time.sleep(2)
                    for i in range(2):
                        dict_now = getWeatherDictionary(url)
                        if dict_now:  # 如果合法json，下一步取得程度
                            if dict_now['HeWeather6'][0]['status'] == 'ok':
                                str_result = getStrFromWeatherDict(str_result, dict_now)
                            print('In retry two:', str_result)
                            break  # 试了3次dict_now，如果行，则给str_result赋值，如果不行，str_result就为空字符串
            print('str_result:', str_result)            
            with open('weather.dat', 'r+b') as f:
                with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)) as m:
                    try:
                        m.seek(0)
                        str_result.rjust(1024, '\x00')
                        bytes_result = str_result.encode(encoding = 'utf-8')  # 将str类型的s转变为bytes类型
                        m.write(bytes_result)  # 写入共享文件（weather.dat）
                        m.flush()
                    except Exception as err:
                        print(repr(err))
                m.close()
            f.close()
    timer = threading.Timer(60, runWeather2Server)  # 每隔3600秒执行一次获取weather2数据
    timer.start()
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
