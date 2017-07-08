#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class vehicle():
  def __init__(self, kind, date, hour):
    self.kind = kind
    self.date = date
    self.hour = hour
    

  def be_driven(self):
    speed = 20 /self.hour
    print '老妈 %s 骑 %s 去买菜，平均速度为 %0.2f km/h' %(self.date, self.kind, speed)

def main():
  vehicle1 = vehicle('电动车', '周一', 0.5)
  vehicle1.be_driven()
  vehicle2 = vehicle('自行车', '周二', 2)
  vehicle2.be_driven()
  vehicle3 = vehicle('电动车', '周三', 0.6)
  vehicle3.be_driven()



if __name__ == '__main__':
  main()
