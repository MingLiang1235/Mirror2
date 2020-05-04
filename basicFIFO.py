#!/usr/bin/python3
#-*- coding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  basicFIFO.py 
#   Perporse:  基本先进先出队列（继承自list）
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-23
######################################################################

class FIFO(list):
	####################################
	# 使用队列的最大长度和初始队列元素列来初始化队列
	####################################	
	def __init__(self, sizeLimit, ls):
		#self.fifo = []
		self.sizeLimit = sizeLimit     #如果ls大于sizeLimit，则会否有问题出现。同样如果ls小于sizeLimit，是否同样会有问题出现
		#self.sizeLimit = len(ls)        #sizeLimit 与 ls长度相等 最好别这么用。等于提出默认限制，最好是明确显式提出限制。
		for i in ls :
			self.push(i)

	####################################
	# 加入一个item。如果溢出去掉打头的item。
	####################################
	def push(self, item):
		if len(self)< self.sizeLimit:
			self.append(item)
		else:
			self.pop()
			self.append(item)
	####################################
	# 弹出一个item并返回该item。如果已经为空则返回空。
	####################################
	def pop(self):
		if self != []:
			temp = self[0]
			del self[0]
			return temp
		else:
			return None

	# def pop(self):
	# 	self.popit()

	####################################
	# 获得所有的内容。
	####################################
	def getAll(self):
		return self
	####################################
	# 队列长度
	####################################
	def getLen(self):
		return len(self)
	####################################
	# 队列是否为空
	####################################
	def isEmpty(self):
		return self == []
	####################################
	# 重新设定限定大小
	####################################
	def setLimit(self, v):
		self.sizeLimit = v