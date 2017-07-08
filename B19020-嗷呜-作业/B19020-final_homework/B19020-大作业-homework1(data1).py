#!/usr/bin/python
# -*- coding: utf-8 -*-
#author AoWu

# 1. 读取文件
import codecs
import os

# 1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        word_list.extend(words)
	return word_list
# 2. 清洗文件
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower() 

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(wd)
	return word_list

# 3. 统计数目

def statistics_words(words):
	s_words_dict = {}
	for word in words:
		if s_words_dict.has_key(word):
			s_words_dict[word] = s_words_dict[word] + 1
		else:
			s_words_dict[word] = 1
	return s_words_dict

# 4. 输出csv文件


def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()



# print
def main():
	words = read_file('data1/dt01.txt')
	print '获取未格式化的单词 %d 个' % (len(words))

	print '获取已格式化单词 %d 个' % (len(format_words(words)))
 	
 	print statistics_words(format_words(words))

 	words_dict = statistics_words(format_words(words))

 	print_to_csv(words_dict, 'dt1.csv')







if __name__ == '__main__':
    main()