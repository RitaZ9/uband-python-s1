#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

def main():
  #01. /
  number = 8 / 5
  print 'number: %d' % (number)

  #02. //
  number = 17//3.0
  print 'number: %d' % (number)

  #03. >>
  number = 15 >> 1
  print 'number = %d' % (number)

  #04. >=
  x = 9
  y = 8
  if(x >= y):
    print '啦啦啦'

if __name__ == '__main__':
  main()