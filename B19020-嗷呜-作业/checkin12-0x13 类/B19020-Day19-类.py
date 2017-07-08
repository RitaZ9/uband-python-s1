#!/usr/bin/python
# -*- coding: utf-8 -*
# author: AoWu

class Cat():
	def __init__(self, name, location, fur_color):
		self.name = name
		self.location = location
		self.fur_color = fur_color

	def scream(self):
		print '来自 %s 的 %s 猫 %s 开始嘶吼' %(self.location, self.fur_color, self.name)


def main():
	qq = Cat('qq', '青海', '黑')
	qq.scream()

if __name__ == '__main__':
  main()

