# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
######################################################################
#   FileName:  window_loop.py   ver.0.1
#   Perporse:  在窗口中滚动字符串跑马灯
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-05-13
######################################################################
#--------------------------------------------------
# 取得窗口中的字符串(窗口宽度, 原字符串, 原字符串指针)
# 注意len(origi_string)一定要大于win_width，即窗口宽度小于字串长度
# index < len(origi_string)
#--------------------------------------------------
def getStringWithWindow(win_width, origi_string, index):
	win_width += 1  # 窗口放大一格 
	#gap = 2  # 字串与字串的间隔
	#origi_string = origi_string + ' ' * gap  # 实现字串间间隔
	length = len(origi_string)
	sub_string = origi_string[index:index+win_width]
	# if length - index -2 < win_width:  # 字串末尾到新字串头中间有两个空格
	if length - index < win_width:
		# sub_string += '  '
		sub_string += origi_string[0:win_width+index-length]
	# else:
	# 	sub_string = sub_string[win_width:]
	return sub_string

