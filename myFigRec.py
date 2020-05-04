#!/usr/bin/python3
#-*- coding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  myFigRec.py 
#   Perporse:  保存画方块曲线图所需要的数据，形成MyFigRec类（对象）
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-23
######################################################################
import random
import psutil
from basicFIFO import FIFO
####################################
# MyFigRec used to content fig and diagrames draw data
####################################
class MyFigRec(object):
	
	# class property
	# size = (200,100)
	Interval = 5.0           #Interval of seconds (采样频率)

	def __init__(self, width=200, height=100):
		
		self.dictCurrSys = {"cpu_percent":0.0, "mem_percent":0.0}     # cpuPercent:float,memPercent:float
		self.size = (width, height)
		self.width = width
		self.height = height
		
		#print "Percent = %f"% (self.getPercent()) 
		
		self.curveVValues = FIFO(10,[])  #这个10只是一个初始值，并没有什么卵用。
		
	####################################
	# 改变（初始化）curveVValues大小（最大大小），一定要做这一步，否则就是10.
	####################################
	def setCurveLimit(self, maxLimit):  # maxLimit: int, max limit value of basicFIFO.FIFO
		self.curveVValues.setLimit(maxLimit)
	####################################
	# 将当前dictCurrSys填入curveVValues(有了一个红头子弹，有了一个白头火药，装填入弹夹)
	####################################
	def pushCurve(self):
		cpu_v = round(self.height*(1-self.dictCurrSys['cpu_percent']))
		mem_v = round(self.height*(1-self.dictCurrSys['mem_percent']))
		dict_v = {"cpu_v":cpu_v, "mem_v":mem_v}
		self.curveVValues.push(dict_v)
	####################################
	# 返回当前对象的curveVValues字段
	####################################
	def getCurve(self):
		return self.curveVValues
	####################################
	# 获得当前cpu_percent (随机伪数据版) 私有函数
	####################################	
	def invokeCpuPercent_fake(self):
		#random.seed()
		return random.random()
	####################################
	# 获得当前mem_percent (随机伪数据版) 私有函数
	####################################	
	def invokeMemPercent_fake(self):
		#random.seed()
		return random.random()
	####################################
	# 获得当前mem_percent (随机伪数据版) 公有函数，对外服务
	####################################
	def invokeDictCurrSys(self):
		try:
			self.dictCurrSys['cpu_percent'] = self.invokeCpuPercent()
			self.dictCurrSys['mem_percent'] = self.invokeMemPercent()
			return True
		except Exception as err:
			print("!"*10 + repr(err))
			return False
	####################################
	# 返回当前cpu_percent 公有函数
	####################################
	def getCurrCpuPercent(self):
		return self.dictCurrSys['cpu_percent']
	####################################
	# 返回当前mem_percent 公有函数
	####################################
	def getCurrMemPercent(self):
		return self.dictCurrSys['mem_percent']
	####################################
	# 返回当前cpu 垂直坐标 公有函数
	####################################
	def getCpuV(self):
		return round(self.height*(1-self.dictCurrSys['cpu_percent']))
	####################################
	# 返回当前mem 垂直坐标 公有函数
	####################################
	def getMemV(self):
		return round(self.height*(1-self.dictCurrSys['mem_percent']))
	####################################
	# 返回FigRec长度（即curveVValues长度) 公有函数
	####################################
	def getFrLen(self):
		return len(self.curveVValues)
	####################################
	# 获得当前电脑cpu_percent  私有函数
	####################################	
	def invokeCpuPercent(self):
		cpu = psutil.cpu_percent(interval=0.5) / 100  # interval太低会不会影响性能
		#print('Cpu_percent_from_machine:'+str(cpu))
		return cpu
	####################################
	# 获得当前电脑cpu_percent  私有函数
	####################################	
	def invokeMemPercent(self):
		mem = psutil.virtual_memory().percent / 100
		#print('Mem_percent_from_machine:'+str(mem))
		return mem



	
	