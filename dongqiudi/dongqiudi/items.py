# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongqiudiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    release_time = scrapy.Field()  # 发表时间
    author = scrapy.Field()  # 作者
    content = scrapy.Field()  # 新闻内容
    crawl_time = scrapy.Field()  # 抓取时间
    from_url = scrapy.Field()  # 来源URL信息
    image_urls = scrapy.Field()  # 图片URL信息
    images = scrapy.Field()  # 图片
    image_paths = scrapy.Field() # 图片路径