# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class TubatuScrapyProjectPipeline:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        myclient.admin.authenticate("admin", "123456")
        mydb = myclient['db_tubatu']
        self.mycollection = mydb['collection_tubatu']


    def process_item(self, item, spider):
        data = dict(item)
        self.mycollection.insert_one(data)
        # print('这是我们获取到的数据item', item)
        return item

class TubatuImagePipeline(ImagesPipeline):
    # def get_media_requests(self, item, info):
    #     pass

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        return item

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name