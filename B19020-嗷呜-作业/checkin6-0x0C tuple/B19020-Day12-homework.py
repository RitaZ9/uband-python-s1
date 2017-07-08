#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: AoWu

def main():
  tup = (1,2,3,4)

  #取值
  print tup[3]

  # 切片
  print tup[1 : 4]
  # 是否存在某值
  print (5 in tup)
  print (3 in tup)
  # 赋值
  e, d, q, p = tup
  print e
  print d
  print q
  print p
  # 遍历
  print '................'
  for item in tup:
    print item
  print '++++++++++++++++'
  for index, item in enumerate(tup):
    print index
    print item


  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(21)
    del tup[3]
    tup[2] = 'it'
  except Exception, e:
    print e

  
if __name__ == '__main__':
  main()


