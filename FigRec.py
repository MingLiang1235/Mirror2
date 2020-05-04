#coding:utf-8

import random
import basicFIFO

class MyFigRec(object):
	'''MyFigRec used to display the fig and diagrames.'''
	
	# class property
	Size = (200,100)
	Interval = 5.0           #Interval of seconds (采样频率)

	def __init__(self):
		
		self.MemInfo = ['--',0,0,0,0.0,0.0]     # self.AppName,self.AvailPhys,self.TotalPhys,self.UsedPhys,percent,cpuPercent(int)
		self.URL = ''
		self.Type = ''
		width,height = self.Size
		self.Position = (0,0)
		self.pos = (0,0)
		self.cpuPos = (0,0)
		
		#print "Percent = %f"% (self.getPercent()) 
		
		self.curLines = basicFIFO.FIFO(10,[])  #这个10只是一个初始值，并没有什么卵用。
		self.curCpuLines = basicFIFO.FIFO(10,[])

	# def __init__(self,memInfo,appName):  #memInfo is list and have 3 values which is AvaliPhys, TotalPhys, UsedPhys
	# 	# instance property
	# 	self.AppName = appName
	# 	self.AvailPhys = memInfo[0]  #memInfo.AvailPhys
	# 	self.TotalPhys = memInfo[1]  #memInfo.TotalPhys
	# 	self.UsedPhys = memInfo[2]   #memInfo.UsedPhys
	# 	#self.Percent = float
	# 	self.Percent = float(self.UsedPhys) / self.TotalPhys
	# 	self.MemInfo = [appName] + memInfo + [self.Percent]

	def getCurrPoint(self):
		w,h = self.Size
		h = h*self.getPercent() 
		return (w,h)

	def getMemInfo(self):
		return self.MemInfo

	def setMemInfo(self,memInfo):
		self.MemInfo = memInfo[:]

	def getAppName(self):
		return self.MemInfo[0]

	# def setAppName(self,appName):
	# 	self.MemInfo[0] = appName

	def getAvailPhys(self):
		return self.MemInfo[1]

	def getTotalPhys(self):
		return self.MemInfo[2]

	def getUsedPhys(self):
		return self.MemInfo[3]

	def getPercent(self):
		return (1-self.MemInfo[4])

	def getCpuPercent(self):
		return (1-self.MemInfo[5])

	def getPercent1(self):
		random.seed()
		#return self.Percent
		return random.random()
	def getCpuPos(self):
		return self.cpuPos

	def setCpuPos(self,point):
		self.cpuPos = point 

	def getPos(self):
		return self.pos

	def setPos(self,point):
		self.pos = point

	def getCurLines(self):
		return self.curLines

	def getCurCpuLines(self):
		return self.curCpuLines

	def setURL(self,url):
		self.URL = url

	def getURL(self):
		return self.URL

	def getType(self):
		return self.Type

	def setType(self,Type):
		self.Type = Type



	
	