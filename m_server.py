#!/usr/bin/python3
#-*- encoding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  m_server.py   ver.0.1
#   Perporse:  Get money data from user and put it to share file.
#	Author:  Jishan                  
#   Email:  unicoder@sohu.com
#	Date:  2020-04-20
######################################################################
import mmap
import contextlib
####################################
# to clear share data file with \x00
####################################
def cleanShareFile(fName):
	with open(fName, "wb") as f:
			fill = '\x00' * 1024
			fill = fill.encode(encoding='utf-8')  # turns str to bytes and write to file.
			f.write(fill)  # turns str to bytes and write to file.
			f.close()
####################################
# write money data to data file
####################################
def writeDataToShareFile(fName, money_dictionary):
	with open(fName,'r+b') as f:   
		with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)) as m:
			try:
				m.seek(0)
				outp_string = 'Pufa:' + str(money_dictionary['pufa']) + \
							'|Lingqian:' + str(money_dictionary['lingqian']) + \
							'|Qita:' + str(money_dictionary['qita'])
				outp_string.rjust(1024, '\x00')  # 右对齐outp_string为\x00
				outp_bytes = outp_string.encode(encoding='utf-8')  # 将str类型转变为bytes类型
				m.write(outp_bytes)
				m.flush()
				print(u"写入成功!")
			except Exception as err:
				print('!'*10 + repr(err))  # 获取完整的err信息。
			m.close()
		f.close()

####################################
# main flow 输入数字并存储于共享数据文件
####################################
print(u"请输入数字：")
lingqian = input(u"微信零钱:")
pufa = input(u"浦发:")
qita = input(u"其他零钱:")
money_diction={'lingqian':lingqian, 'pufa':pufa, 'qita':qita}

fName = ".\money.dat"
cleanShareFile(fName)
writeDataToShareFile(fName, money_diction)