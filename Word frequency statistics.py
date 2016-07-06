#!/usr/bin/python3
# -*- coding: utf-8 -*-

' word frequency statistics'

_author_='wangjianfeng'

#引入一个新的模块，在其中那个string.pounctuation包含了各种标点符号!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
import string
path='E:\\Walden.txt'
with open(path,'r',encoding='utf-8') as text:
    #在文字首位去掉了连在一起的标点符号，并把字母大写的单词转换为小写
    words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    #将列表用set函数转换为集合，自动去掉了其中的所有重复元素
    word_index=set(words)
    #创建了一个以单词为键（key)出现频率为值（value）的字典
    counts_dict={index:words.count(index) for index in word_index}
    #打印整理后的函数，其中key=lambda x: count_dict[x]为lambda表达式，匿名函数
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
    print('{}--{} times'.format(word,counts_dict[word]))