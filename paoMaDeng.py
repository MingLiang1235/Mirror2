#!/usr/bin/python3
# -*- coding: utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n
######################################################################
#   FileName:  paoMaDeng.py   ver.0.1
#   Perporse:  使用跑马灯绘制字符串并显示在Widget中                                          
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-05-15
######################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from weather import getWeather2
from window_loop import getStringWithWindow
#--------------------------------------------------
# 继承自QFrame的跑马灯显示区域类
#-------------------------------------------------- 
class PaoMaArea(QFrame):
	def __init__(self, parent=None):
		super().__init__(parent)  # 先调用父窗口（parent）的初始化程序，再初始化自己。
		self.text = getWeather2()  # 需要跑马的字串
		self.gap = 2  # 两跑马灯字符串中间的间隔
		self.text += ' ' * self.gap
		self.rect = QRect(10, 0, 460, 20)  # 画布方块
		print('In paoMaArea init,self.text:', self.text)
		self.win_width = round(460/15)  # 文字窗口宽度
		self.width = self.rect.width()  # 画布方块宽度
		self.height = self.rect.height()  # 画布方块高度
		self.velocity = -2  # 每次向左位移
		self.count = 0  # 左移一个字母次数
		self.offset = 16  # y的偏移量
		self.pos = 460  # x的初始位置
		self.one_word = 22  # 等于16为左移一个字母
		self.text1 = self.text  # 用text初始化text1
		self.round_times = 0  # paintEvent计数，用于几分钟重新调用一下getWeather2
	#--------------------------------------------------
	# All user drawing is in paintEvent: 由主程序决定，每0.2秒显示一次，向左跑马灯
	#--------------------------------------------------
	def paintEvent(self, event):  
		#print('In PaoMaArea paintEvent.')
		self.round_times += 1
		if self.round_times > 3000:  # 每十分钟调用一次，获取最新天气跑马数据。
			self.text = getWeather2()
			self.text += ' ' * self.gap
			print('In PaoMaArea paint:', self.text)
			self.round_times = 0  # 计数器清零
		painter = QPainter(self)
		#font = QFont('宋体', 25, QFont.Bold, True)
		font = QFont('SimSun', 16)
		# font.setPointSize(15)
		font.setBold(True)
		# font.setWeight(75)
		#painter.setFont(QFont('SimSun', 20))
		painter.setFont(font)
		painter.setPen(QColor(255, 255, 255))

		# painter.fillRect(self.rect, QColor(0, 63, 125))  # 清空画布，使用天蓝色填充
		x = self.pos
		for i, c in enumerate(self.text1):
			char_size = painter.fontMetrics().size(Qt.TextSingleLine, c)
			char_width = char_size.width()
			if x > self.width:
				break
			if x + char_width < 0:
				x += char_width
				continue
			y = self.offset
			painter.drawText(x, y, c)
			#painter.drawText(self.rect, Qt.AlignCenter, self.text)
			x += char_width
		self.pos += self.velocity
		self.one_word += self.velocity
		if self.pos < 0:	
			if self.one_word < 0:
				index = self.count % len(self.text)  # 指针是向左移动字母数与原字串求余得到的
				self.text1 = getStringWithWindow(self.win_width, self.text, index)  # win_width, origi_string, index
				#print('self.win_width:', self.win_width, 'index:', index, 'self.text:', self.text1)
				self.count += 1
				# self.one_word = 22  # self.one_word恢复原值
				self.one_word = painter.fontMetrics().size(Qt.TextSingleLine,self.text1[0]).width()  # 按text1的第一个字符赋值字宽。
				#print('one_word:', self.one_word)
				self.pos = 0