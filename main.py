#!/usr/bin/python3
# -*- coding: utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n
# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
######################################################################
#   FileName:  main.py   ver.0.5
#   Perporse:  Draw frame of prog,get data from multiple source
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################
import sys
import threading
import pigpio
from clock import getTime
from money import getMoney
from weather import getWeather
from schema import PaintArea
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet("background-color: rgb(0, 63, 125); ")  # 天蓝色
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_datetime = QtWidgets.QLabel(self.centralwidget)
        self.label_datetime.setGeometry(QtCore.QRect(100, 0, 320, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_datetime.setFont(font)
        self.label_datetime.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_datetime.setObjectName("label_datetime")
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_1.setGeometry(QtCore.QRect(0, 30, 241, 161))
        self.widget_1.setObjectName("widget_1")
        self.today_temp = QtWidgets.QLabel(self.widget_1)
        self.today_temp.setGeometry(QtCore.QRect(30, 0, 105, 71))
        font = QtGui.QFont()
        font.setFamily("文泉驿点阵正黑")
        font.setPointSize(36)
        # font.setBold(True)
        font.setWeight(75)
        self.today_temp.setFont(font)
        self.today_temp.setStyleSheet("color: rgb(255, 255, 255);")
        self.today_temp.setObjectName("today_temp")
        self.today_weather = QtWidgets.QLabel(self.widget_1)
        self.today_weather.setGeometry(QtCore.QRect(30, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.today_weather.setFont(font)
        self.today_weather.setStyleSheet("color: rgb(255, 255, 255);\n"
"style=\"text-align:center\"")
        self.today_weather.setObjectName("today_weather")
        self.today_wind_3 = QtWidgets.QLabel(self.widget_1)
        self.today_wind_3.setGeometry(QtCore.QRect(200, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.today_wind_3.setFont(font)
        self.today_wind_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.today_wind_3.setObjectName("today_wind_3")
        self.today_weather_2 = QtWidgets.QLabel(self.widget_1)
        self.today_weather_2.setGeometry(QtCore.QRect(30, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.today_weather_2.setFont(font)
        self.today_weather_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.today_weather_2.setObjectName("today_weather_2")
        self.curr_city = QtWidgets.QLabel(self.widget_1)
        self.curr_city.setGeometry(QtCore.QRect(140, 0, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.curr_city.setFont(font)
        self.curr_city.setStyleSheet("color: rgb(255, 255, 255);")
        self.curr_city.setObjectName("curr_city")
        self.day_1 = QtWidgets.QLabel(self.centralwidget)
        self.day_1.setGeometry(QtCore.QRect(10, 200, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.day_1.setFont(font)
        self.day_1.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.day_1.setObjectName("day_1")
        self.day_2 = QtWidgets.QLabel(self.centralwidget)
        self.day_2.setGeometry(QtCore.QRect(10, 240, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.day_2.setFont(font)
        self.day_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.day_2.setObjectName("day_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(270, 31, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_1.setObjectName("label_1")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 40, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.day_1_wind_4 = QtWidgets.QLabel(self.centralwidget)
        self.day_1_wind_4.setGeometry(QtCore.QRect(260, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.day_1_wind_4.setFont(font)
        self.day_1_wind_4.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.day_1_wind_4.setObjectName("day_1_wind_4")
        self.money_1 = QtWidgets.QLabel(self.centralwidget)
        self.money_1.setGeometry(QtCore.QRect(340, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.money_1.setFont(font)
        self.money_1.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.money_1.setObjectName("money_1")
        self.money_2 = QtWidgets.QLabel(self.centralwidget)
        self.money_2.setGeometry(QtCore.QRect(340, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.money_2.setFont(font)
        self.money_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.money_2.setObjectName("money_2")
        self.money_3 = QtWidgets.QLabel(self.centralwidget)
        self.money_3.setGeometry(QtCore.QRect(340, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.money_3.setFont(font)
        self.money_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.money_3.setObjectName("money_3")
        #self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2 = PaintArea(self)  # 使用self作为PaintArea的父窗口初始化self.widget_2
        self.widget_2.setGeometry(QtCore.QRect(260, 160, 211, 111))
        self.widget_2.setObjectName("widget_2")
        #self.widget_2.move(260,160)  # 绝对定位
        self.label_9.raise_()
        self.label_datetime.raise_()
        self.widget_1.raise_()
        self.day_1.raise_()
        self.day_2.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.day_1_wind_4.raise_()
        self.money_1.raise_()
        self.money_2.raise_()
        self.money_3.raise_()
        self.widget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_datetime.setText(_translate("MainWindow", "DATE TIME"))
        self.today_temp.setText(_translate("MainWindow", "25°"))
        self.today_weather.setText(_translate("MainWindow", "雷阵雨"))
        self.today_wind_3.setText(_translate("MainWindow", "风力"))
        self.today_weather_2.setText(_translate("MainWindow", "。。。/。。。"))
        self.curr_city.setText(_translate("MainWindow", "北京"))
        self.day_1.setText(_translate("MainWindow", "...."))
        self.day_2.setText(_translate("MainWindow", "...."))
        self.label_1.setText(_translate("MainWindow", "Money"))
        self.label_9.setText(_translate("MainWindow", "__________________________"))
        self.label_2.setText(_translate("MainWindow", "微信零钱:"))
        self.label_3.setText(_translate("MainWindow", "浦发:"))
        self.day_1_wind_4.setText(_translate("MainWindow", "零钱:"))
        self.money_1.setText(_translate("MainWindow", "...."))
        self.money_2.setText(_translate("MainWindow", "...."))
        self.money_3.setText(_translate("MainWindow", "...."))
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.label_datetime.setAlignment(QtCore.Qt.AlignCenter)
        
        self.dict_config = self.getConfig()
        #print('self.dict_config:',self.dict_config)
        if self.dict_config['fullscreen'] == 'True':
            #print('Before fullScreen , in dict==True')
            self.showFullScreen()
            self.fullScreenFlag = 1
        self.update_second()
        self.update_money()
        self.update_weather()
        self.update_schema()
    
        self.prev_tick = 100000000
        pin = 12
        pi = pigpio.pi()
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_UP)
        
        self.cb = pi.callback(pin, pigpio.FALLING_EDGE, self.cbf)    
        #self.init_gpio()
        #self.drawSchema = drawSchema(self.widget_2)
    
    def cbf(self, gpio, level, tick):
        print(gpio, level, tick)
        if (tick - self.prev_tick)> 500000:
            #print('self.fullScreenFlag:', \
			#	self.fullScreenFlag)
            self.prev_tick = tick
            if self.fullScreenFlag ==1:
                self.showNormal()
                self.fullScreenFlag = 0
            else:
                self.showFullScreen()
                self.fullScreenFlag = 1

    def closeEvent(self, event):
        self.cb.cancel()

   # def init_gpio(self):
    #    timer5 = threading.Timer(5, self.init_gpio)
     #   timer5.start()

    def getConfig(self):
        dict_config = {}
        for line in open(r'./config'):
            #print(line)
            key,value = (line.strip()).split(':')
            dict_config[key] = value
        return dict_config

    def update_second(self):
        _translate = QtCore.QCoreApplication.translate
        date_time = getTime()
        self.label_datetime.setText(_translate("MainWindow", date_time))
        timer1 = threading.Timer(1, self.update_second)
        timer1.start()

    def update_money(self):
        _translate = QtCore.QCoreApplication.translate
        dict_money = getMoney()
        self.money_1.setText(_translate("MainWindow", dict_money["Lingqian"]))
        self.money_2.setText(_translate("MainWindow", dict_money["Pufa"]))
        self.money_3.setText(_translate("MainWindow", dict_money["Qita"]))
        timer2 = threading.Timer(3600, self.update_money)
        timer2.start()

    def update_weather(self):
        _translate = QtCore.QCoreApplication.translate
        dict_weather = None 
        try:
            dict_weather = getWeather()
        except Exception as err:
            print(repr(err))

        if dict_weather:
            self.today_temp.setText(_translate("MainWindow",dict_weather['now']['tmp']+chr(0x2103)))  # python2:unichr()
            self.curr_city.setText(_translate("MainWindow",dict_weather['city']))
            self.today_weather.setText(_translate("MainWindow",dict_weather['now']['cond_txt']))
            self.today_weather_2.setText(_translate("MainWindow",dict_weather['now']['tmp_min']+'/'+ \
                    dict_weather['now']['tmp_max']+' '+dict_weather['now']['wind_dir']+' '+ \
                    dict_weather['now']['wind_sc']))
            for i in range(len(dict_weather['three_day'])):
                if i == 0:
                    self.day_1.setText(_translate("MainWindow", dict_weather['three_day'][i]['date']+' '+ \
                        dict_weather['three_day'][i]['cond_txt_d']+' '+ \
                        dict_weather['three_day'][i]['tmp_min']+'/'+ \
                        dict_weather['three_day'][i]['tmp_max']+' '+ \
                        dict_weather['three_day'][i]['wind_dir']+ \
                        dict_weather['three_day'][i]['wind_sc']))
                elif i == 1:
                    self.day_2.setText(_translate("MainWindow", dict_weather['three_day'][i]['date']+' '+ \
                        dict_weather['three_day'][i]['cond_txt_d']+' '+ \
                        dict_weather['three_day'][i]['tmp_min']+'/'+ \
                        dict_weather['three_day'][i]['tmp_max']+' '+ \
                        dict_weather['three_day'][i]['wind_dir']+ \
                        dict_weather['three_day'][i]['wind_sc']))
        timer3 = threading.Timer(3600, self.update_weather)
        timer3.start()

    def update_schema(self):
        #self.widget_2.show()
        self.widget_2.update()  # 重绘widget_2
        timer4 = threading.Timer(3, self.update_schema)  # 每3秒重绘一次cpu和mem
        timer4.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    #sys.exit(app.exec_())
    app.exec_()
