#!/usr/bin/python
# -*- coding: utf-8 -*-
#author AoWu

# 1. 读取文件
import codecs
import os

# 1. 读取文件

def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_paths.append(file_path)
	return file_paths


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")
        words = word_split(words)
        word_list.extend(words)
    return word_list



def read_files(file_paths):
	final_words = []
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words



# 2. 清洗文件


def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
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

def word_split(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list
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
	words = read_files(get_file_from_folder('data2'))

	print '获取未格式化的单词 %d 个' % (len(words))

	print '获取已格式化单词 %d 个' % (len(format_words(words)))

	print statistics_words(format_words(words))

	words_dict = statistics_words(format_words(words))

	print_to_csv(words_dict, 'dt2.csv')







if __name__ == '__main__':
    main()