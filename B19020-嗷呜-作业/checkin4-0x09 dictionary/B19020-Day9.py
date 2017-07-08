#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: AoWu

# 作业1 
def main():
	dictionary = {
				'orange' : 'my second favorite color',
				'mango' : 'my favorite fruit',
				'hot egg' : 'my favorite food'
				}
	print len(dictionary)
	print dictionary.keys()
	print dictionary.values()
	print dictionary.has_key('orange')
	print dictionary.has_key('apple')

	dictionary['apple'] = "the fruit and Adam and Eve were not allowed to eat "
	print dictionary

	del dictionary['apple']
	print dictionary
	print len(dictionary)


	print '...............'
	print dictionary['hot egg']
	if dictionary.has_key('apple'):
		print dictionary['apple']
	else:
		print '很抱歉找不到这个单词呀'
	print '====================='

	for key in dictionary.keys():
		print key
		print dictionary[key]





if __name__ == '__main__':
  main()