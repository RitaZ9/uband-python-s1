#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: AuWu

def shopping():
	good_price = 6
	resonable_price = 5
	buy_amount = 2

	who = 'AuWu的娘亲'
	good_description = "西双版纳大白菜"

	is_cheap = False

	print "%s 上街看到了 %s， 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= resonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (resonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap, buy_amount, good_price

def talk(is_cheap, buy_amount, good_price):
	if is_cheap:
		print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了 %d 斤”。' % (buy_amount)
	else:
		print '老妈回到家里，跟老爸说：“今天去买菜，菜好贵贵哟，没买”。'

def note(is_cheap, buy_amount, good_price):
	if is_cheap:
		total_price = buy_amount * good_price
		print '老妈在小本子上记了买菜花销 %d 元'% (total_price)

def main():
	is_cheap, buy_amount, good_price = shopping()
	talk(is_cheap, buy_amount, good_price)
	note(is_cheap, buy_amount, good_price)

if __name__ == '__main__':
  main()