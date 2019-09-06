# -*- coding: utf-8 -*-
import re

import scrapy
from spider.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['id'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['name'] = i_item.xpath(
                ".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            douban_item['url'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/@href").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            content_genre = "".join(content[1].split())
            douban_item['time'] = content_genre.split("/")[0]
            douban_item['country'] = content_genre.split("/")[1]
            douban_item['genre'] = content_genre.split("/")[2]
            content_director = "".join(content[0].split())
            director = content_director.split("主演")[0].split(":")[1].split("/")[0]
            # 去除英文和其他字符
            douban_item['director'] =  re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", director)
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()[:-3]
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']//span/text()").extract_first()
            yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
