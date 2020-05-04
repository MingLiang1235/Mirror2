#!/usr/bin/python3
#-*- coding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  test_myFigRec.py 
#   Perporse:  测试保存画方块曲线图所需要的数据，即测试MyFigRec类
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-24
######################################################################
from myFigRec import *
fr = MyFigRec()
print("CurrCpu:"+str(fr.getCurrCpuPercent()))
print("CurrMem:"+str(fr.getCurrMemPercent()))
print("curveVValues.sizeLimit:"+str(fr.curveVValues.sizeLimit))
fr.setCurveLimit(21)
print("curveVValues.sizeLimit:"+str(fr.curveVValues.sizeLimit))
if fr.invokeDictCurrSys():
	print("CurrCpu:"+str(fr.getCurrCpuPercent()))
	print("CurrMem:"+str(fr.getCurrMemPercent()))
else:
	print("Can not invoke dictCurrSys.")
fr.pushCurve()
print("getCurve:"+str(fr.getCurve()))
fr.invokeDictCurrSys()
fr.pushCurve()
fr.invokeDictCurrSys()
fr.pushCurve()
print("After 3 input, getCurve:"+str(fr.getCurve()))
print("Now CurrCpu:"+str(fr.getCurrCpuPercent()))
print("Now cpu_v:"+str(fr.getCpuV()))
print("Now CurrMem:"+str(fr.getCurrMemPercent()))
print("Now mem_v:"+str(fr.getMemV()))
print("Now fr len:"+str(fr.getFrLen()))