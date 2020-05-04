#!/usr/bin/python3
#-*- encoding:UTF-8 -*-
#以上保存后在linux内无法直接打开，需要vim :set fileformat=unix来去除\r\n为\n

#coding=utf-8
######################################################################
#   FileName:  test_money.py 
#   Perporse:  Test money.py
#   Author:  Jishan                  
#   Email:  unicoder@sohu.com
#   Date:  2020-04-21
######################################################################
from money import getShareFileContent
from money import getMoney
print(getShareFileContent())
print(getMoney())