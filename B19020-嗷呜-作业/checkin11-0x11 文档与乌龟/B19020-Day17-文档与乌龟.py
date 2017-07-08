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
  # test 1
  turtle.position()
  (0.00, 0.00)
  bree.forward(500)
  bree.fd(-700)

  # test 2
  bree.right(60)
  bree.heading()
  560.0
  bree.fd(70)

  # test 3
  bree.circle(150,200)
  turtle.position()
  (0.00, 200.00)
  turtle.heading()
  180
  turtle.fd(250)

if __name__ == '__main__':
  main()