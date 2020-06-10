# -*- coding: utf-8 -*-
import json
from datetime import datetime

import scrapy

from items import DongqiudiItem


class CrawlDongqiudiSpider(scrapy.Spider):
    name = 'crawl_dongqiudi'
    allowed_domains = ['dongqiudi.com']
    # start_urls = ['http://dongqiudi.com/']
    count = 1
    def parse(self, response):
        pass

    def start_requests(self):
        url_list = [
            'https://www.dongqiudi.com/api/app/tabs/web/1.json',  # 头条
            'https://www.dongqiudi.com/api/app/tabs/web/56.json',  # 中超
            'https://www.dongqiudi.com/api/app/tabs/web/3.json',  # 英超
            'https://www.dongqiudi.com/api/app/tabs/web/5.json',  # 西甲
            'https://www.dongqiudi.com/api/app/tabs/web/4.json',  # 意甲
            'https://www.dongqiudi.com/api/app/tabs/web/6.json',  # 德甲
            'https://www.dongqiudi.com/api/app/tabs/web/55.json',  # 深度
            'https://www.dongqiudi.com/api/app/tabs/web/57.json',  # 国际
            'https://www.dongqiudi.com/api/app/tabs/web/37.json',  # 闲情
        ]
        for url_item in url_list:
            # print(url_item)
            yield scrapy.Request(url=url_item, callback=self.handle_page_response, encoding='utf-8', dont_filter=True)

    def handle_page_response(self, response):
        self.count += 1
        data = json.loads(response.text)
        articles = data['articles']
        for article in articles:
            article_info = {}
            article_info['title'] = article['title']   # 标题
            article_info['release_time'] = article['published_at']  # 发表时间
            if 'author' in article:
                article_info['author'] = article['author']['name']
            else:
                article_info['author'] = ''
            article_info['content'] = article['title']  # 新闻内容
            article_info['crawl_time'] = str(datetime.now())  # 抓取时间
            article_info['from_url'] = article['share']  # 来源URL信息
            article_info['image_urls'] = article['thumb']  # 图片URL信息
            article_info['images'] = article['thumb']  # 图片
            article_info['image_paths'] = 'images' # 图片路径
            yield scrapy.Request(url=article_info['from_url'], callback=self.handle_detail, dont_filter=True, meta=article_info)
        next = data['next']
        if next and self.count <= 2:
            yield scrapy.Request(url=next, callback=self.handle_page_response, dont_filter=True)

    def handle_detail(self, response):
        article_info = DongqiudiItem()
        article_info['title'] = response.request.meta['title']   # 标题
        article_info['release_time'] = response.request.meta['release_time']  # 发表时间
        article_info['author'] = response.request.meta['author']  # 作者
        article_info['content'] = ''.join(response.xpath('//div[@class="con"]//p/text()').extract())
        article_info['crawl_time'] = str(datetime.now())  # 抓取时间
        article_info['from_url'] = response.request.meta['from_url']  # 来源URL信息
        article_info['image_urls'] = response.xpath('//div[@class="con"]//img/@data-src').extract()  # 图片URL信息
        article_info['images'] = response.request.meta['images']  # 图片
        article_info['image_paths'] = 'images' # 图片路径
        yield article_info