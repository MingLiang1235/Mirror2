#!/usr/bin/python3
# -*- coding: utf-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n
######################################################################
#   FileName:  test_schema.py   ver.0.1
#   Perporse:  Test draw schema of cpu and memory used graph
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-23
######################################################################
import sys
from schema import PaintArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
	text = 'Welcome to programe PyQt!'
	# area = PaintArea()
	def __init__(self,parent=None):
		super(Example,self).__init__(parent)
		self.initUI()
		
	def initUI(self):
		self.area = PaintArea()  # 引入area，在后面show中调用area的paintEvent事件处理程序。
		hbox = QHBoxLayout()
		hbox.addWidget(self.area)

		self.setLayout(hbox)

		self.setGeometry(300,300,300,150)
		self.setWindowTitle('test_schema')
		self.show()
		#self.area.show()  # no need this sentence.

	# def paintEvent(self, event):
	# 	print("In paint event.")
	# 	p = QPainter(self)
	# 	p.begin(self)
 #        # p.setPen(QPen(Qt.red))
 #        # linearGradient = QLinearGradient(0, 0, 50, 50)
 #        # p.setBrush(QBrush(linearGradient))
 #        #rect = QRect(10, 10, 100, 50)
 #        #p.drawLine(rect.topLeft(), rect.bottomRight())
	# 	self.drawText(event,p)
	# 	p.end()

	# def drawText(self,event,qp):
	# 	qp.setPen(QColor(255, 0, 0))
	# 	qp.setFont(QFont('SimSun', 20))
	# 	qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())