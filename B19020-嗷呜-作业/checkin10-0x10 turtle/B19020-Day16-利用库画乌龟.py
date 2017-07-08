#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: AoWu

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('green')

	bree = turtle.Turtle()
	bree.shape('turtle')
	bree.color('red')
	bree.speed(1)

	for i in range(1,10):
		bree.forward(200)
		bree.left(60)
		bree.forward(200)
		bree.left(60)
		bree.forward(50)
		bree.left(60)
		bree.forward(200)

if __name__ == '__main__':
  main()