#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' property '

_author_='wangjianfeng'

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
#test
s=Screen()
s.height=1024
s.width=768
print(s.resolution)
#测试代码正确与否
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution