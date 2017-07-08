#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: AoWu

# 作业1 
def homework1():
	print '老妈来到菜市场'
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	index = 0
	for lst_item in lst:
		if index % 2 == 0:
			print '老妈看到了 %s ， 买了 %d 斤'% (lst_item, index + 1)
		else:
			print '老妈继续逛， 看到 %s 不买'% (lst_item)
		index = index + 1
		

 # 作业2 加三个菜
def homework2():
	print '---------------------'
 	print '老妈来到菜市场'
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺', '黄瓜', '螃蟹', '大蒜']
	index = 0
	for lst_item in lst:
		if index % 2 == 0:
			print '老妈看到了 %s ， 买了 %d 斤'% (lst_item, index + 1)
		else:
			print '老妈继续逛， 看到 %s 不买'% (lst_item)
		index = index + 1


# 作业3 只逛5~9个菜
def homework3():
	print '---------------------'
 	print '老妈来到菜市场'
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺', '黄瓜', '螃蟹', '大蒜']
	lst2 = lst[5 : 10]
	index = 0
	for lst_item in lst2:
		if index % 2 == 0:
			print '老妈看到了 %s ， 买了 %d 斤'% (lst_item, index + 1)
		else:
			print '老妈继续逛， 看到 %s 不买'% (lst_item)
		index = index + 1

if __name__ == '__main__':
  homework1()
  homework2()
  homework3()