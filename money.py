#!/usr/bin/python3
#-*- encoding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  money.py 
#   Perporse:  Get current account money from share data file 
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################
import mmap
import contextlib
####################################
# Get content of share file as string
####################################
def getShareFileContent():
	fName = "./money.dat"
	text = None
	with open(fName,'r') as f:   
		with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)) as m:
			text = m.read(1024)
			text = str(text, encoding='utf-8').replace('\x00', '')
			m.close()
		f.close()
	return text
####################################
# return:{Pufa:100, Lingqian:100, Qita:100}
####################################
def getMoney():
	dic = {}
	text = getShareFileContent()
	ls = text.split("|")
	for item in ls:
		key, value = item.split(":")
		dic[key] = value
	return dic

