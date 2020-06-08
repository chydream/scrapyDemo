# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TubatuScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content_name = scrapy.Field()
    content_id = scrapy.Field()
    content_url = scrapy.Field()
    nick_name = scrapy.Field()
    # pic_url = scrapy.Field()
    image_urls = scrapy.Field()
    pic_name = scrapy.Field()

