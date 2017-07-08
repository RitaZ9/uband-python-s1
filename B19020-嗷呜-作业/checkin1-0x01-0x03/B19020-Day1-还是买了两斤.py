#@/usr/bin/python
# -*- coding: utf-8 -&-
# @author: AoWu

def main():
	who = 'AoWu的娘亲'
	good_price = 6
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price >= reasonable_price:
		print '她认为不便宜'
		is_cheap = False
		print '但她还是买了 %d 斤' % (buy_amount)


if __name__ == '__main__':
  main()
