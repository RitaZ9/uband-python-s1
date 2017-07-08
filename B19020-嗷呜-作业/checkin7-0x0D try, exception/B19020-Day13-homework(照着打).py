#!/usr/bin/python
# -*- coding: utf-8 -*-
# author AoWu

def main():
	week_overnight = [False, False, False, True, False]
	for index, is_overnight in enumerate(week_overnight):
		print '今天星期%d' % (index + 1)

		try:
			overnight_check(is_overnight)
		except Exception, e:
			print '错啦错啦'
			print '老妈骂了老爸一顿，跪了一晚搓衣板'
		else:
			print '什么都没有发生呀'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚啦')
	else:
		print '一切正常'
if __name__ == '__main__':
  main()