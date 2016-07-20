#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'crawler taobaomm'

_author_='wangjianfeng'

import scrapy

class WeatherItem(scrapy.Item):
    #define the fields for your item hers like
    #name=scrapy.Field()
    city=scrapy.Field()
    date=scrapy.Field()
    dateDesc=scrapy.Field()
    dayTemp=scrapy.Field()
    pass
