#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'XML'

_author_='wangjianfeng'

#操作XML，have two way:DOM VS SAX,DOM will read whole into memory,resolved to a tree;SAX is flow pattern,
from xml.parsers.expat import ParserCreate

class DafaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:{},attrs:{}'.format(name,str(attrs)))
        
    def end_element(self,name):
        print('sax:end_element:{}'.format(name))
        
    def char_data(self,text):
        if self.char_data==None:
            pass
        else:
            print('sax:char_data:{}'.format(text))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler=DafaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)