# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class DongqiudiPipeline:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        myclient.admin.authenticate("admin", "123456")
        mydb = myclient['db_dongqiudi']
        self.mycollection = mydb['c_dongqiudi']


    def process_item(self, item, spider):
        # print('这个是我们获取到的数据：{0}'.format(item))
        data = dict(item)
        self.mycollection.insert_one(data)
        return item

class DongqiudiImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("改新闻没有图片")
        return item

    def file_path(self, request, response=None, info=None):
        url = request.url
        item = request.meta['item']['title']
        path = item + "." + url.split('~')[-2].split('.')[-1]
        return path
