#!/usr/bin/python3
# -*- coding: utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n
######################################################################
#   FileName:  schema.py   ver.0.1
#   Perporse:  Draw schema of cpu and memory used graph
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import threading
import time
import math
from myFigRec import *
####################################
# PaintArea is a frame that can draw itself
####################################
class PaintArea(QFrame):
    ####################################
    # Init object of PaintArea
    ####################################
    def __init__(self, parent=None):
        super().__init__(parent)  # 先调用父窗口（parent）的初始化程序，再初始化自己。
        #super().__init__()
        self.text = u"欢迎学习PyQt5"
        #print("In PaintArea init.")
        self.update()
        self.rect = QRect(0, 0, 200, 100)  # 画布方块
        self.width = self.rect.width()  # 画布宽
        self.height = self.rect.height()  # 画布高
        self.penCooldi = QPen(Qt.green)  # 坐标画笔
        self.penCooldi.setWidth(2)
        self.penCpu = QPen(Qt.red)  # cpu画笔（红色的，画CPU）
        self.penCpu.setWidth(2)
        self.penMem = QPen(Qt.green)  # mem画笔（绿色的，画mem）
        self.penMem.setWidth(2)
        self.brushMem = QBrush()  # mem画刷 
        #color = QColor(0, 255, 0, 0.5)       
        self.brushMem.setColor(Qt.cyan)  # 画刷绿的,半透明
        style = Qt.BrushStyle(Qt.SolidPattern)  # 画刷统一颜色
        self.brushMem.setStyle(style)

        # self.firstPaintFlag = False  # 去除QPainter::begin: Painter already active 这句显示
        self.firstPaintFlag = True  # 去除QPainter::begin: Painter already active 这句显示
        self.left = 10  # 每次画图减去的像素数
        self.currHoriValue = math.floor(self.width/self.left + 1)  # 当前横坐标格数(比如21)，每次运行减一。
        self.fr = MyFigRec()
        self.fr.setCurveLimit(self.currHoriValue)
        self.fr.invokeDictCurrSys()  # 先运行一次，提取数据
        self.fr.pushCurve()
    ####################################
    # All user drawing is in paintEvent
    ####################################    
    def paintEvent(self, event):
        #print("In paint event.")
        p = QPainter(self)
        # if self.firstPaintFlag:
        #     #p.begin(self)
        #     self.firstPaintFlag = False
        #self.drawText(event, p)  # 测试:反复重绘当前时间
        self.drawCooldinate(event, p)
        self.drawMem(event, p)
        self.drawCpu(event, p)
        #p.end()
    ####################################
    # Draw text info in center of self.rect
    ####################################
    def drawText(self, event, p):
        p.setPen(QColor(255, 0, 0))
        p.setFont(QFont('SimSun', 20))
        self.text = time.strftime("%Y %H:%M:%S %a", time.localtime())
        #qp.drawText(event.rect(), Qt.AlignCenter, self.text)
        p.drawText(self.rect, Qt.AlignCenter, self.text)
    ####################################
    # Draw cooldinate line and tag
    ####################################
    def drawCooldinate(self, event, p):
        p.setPen(self.penCooldi)  # value=2 画笔线宽2.

        p.drawLine(self.rect.topLeft(), self.rect.bottomLeft())
        p.drawLine(self.rect.bottomLeft(), self.rect.bottomRight())
    ####################################
    # draw cpu curve
    ####################################
    def drawCpu(self, event, p):
        p.setPen(self.penCpu)  # color: Qt.yellow
        #p.drawText(self.rect, Qt.AlignCenter, str(self.fr.curveVValues.sizeLimit))
        points = []
        #self.fr.invokeDictCurrSys()  # 获取新数据
        #self.fr.pushCurve()  # 将新数据压入堆栈
        x = (self.currHoriValue-self.fr.getFrLen()) * self.left  # 第一个坐标点的横坐标
        for item in self.fr.getCurve():
            y = item['cpu_v']
            points.append((x,y))
            x += self.left  # 横坐标向右移一格
        
        for i in range(len(points)-1):
            p.drawLine(points[i][0],
                        points[i][1],
                        points[i+1][0],
                        points[i+1][1])
            
    ####################################
    # draw mem polygon
    ####################################  
    def drawMem(self, event, p):  
        p.setPen(self.penMem)  # color:Qt.green
        p.setBrush(self.brushMem)
        points = []
        self.fr.invokeDictCurrSys()  # 获取新数据
        self.fr.pushCurve()  # 将新数据压入堆栈
        x = (self.currHoriValue-self.fr.getFrLen()) * self.left  # 第一个坐标点的横坐标
        x0 = x
        for item in self.fr.getCurve():
            y = item['mem_v']
            points.append((x,y))
            x += self.left  # 横坐标向右移一格
        points.insert(0, (x0, self.fr.height))
        points.append((self.fr.width, self.fr.height))
        polygon = []
        for i in points:
            polygon.append(QPoint(i[0], i[1]))
        p.drawPolygon(QPolygon(polygon),Qt.WindingFill)
        