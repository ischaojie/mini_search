# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    
    id = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 上映时间
    time = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 简介
    genre = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 评分人数
    evaluate = scrapy.Field()
    # 描述
    describe = scrapy.Field()
