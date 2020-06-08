# -*- coding: utf-8 -*-
import re

import scrapy

from guazi_scrapy_project.handle_mongo import mongo

from guazi_scrapy_project.items import GuaziScrapyProjectItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    # start_urls = ['http://guazi.com/']

    def start_requests(self):
        while True:
            task = mongo.get_task('guazi_task')
            if not task:
                break
            if '_id' in task:
                task.pop('_id')
            print(task['task_url'])
            if task['item_type'] == 'list_item':
                yield scrapy.Request(
                    url=task['task_url'],
                    callback=self.handle_car_item,
                    method='GET',
                    # headers=,
                    # body=,
                    meta=task,
                    # cookies=,
                    encoding='utf-8',
                    # priority=,
                    dont_filter=True,
                    errback=self.handle_err,
                    # flags=
                )
                # yield  scrapy.FormRequest()
            elif task['item_type'] == 'car_info_item':
                yield scrapy.Request(
                    url=task['task_url'],
                    callback=self.handle_car_info,
                    method='GET',
                    # headers=,
                    # body=,
                    meta=task,
                    # cookies=,
                    encoding='utf-8',
                    # priority=,
                    dont_filter=True,
                    errback=self.handle_err,
                    # flags=
                )

    def parse(self, response):
        pass
        # print(response.text)


    def handle_err(self, failure):
        print(failure)
        mongo.save_task('guazi_task', failure.request.meta)


    def handle_car_item(self, response):
        if '中为您找到0辆好车' in response.text:
            return
        car_item_list = response.xpath("//ul[@class='carlist clearfix js-top']/li")
        # print(car_item_list)
        for car_item in car_item_list:
            car_list_info = {}
            car_list_info['car_name'] = car_item.xpath("./a/h2/text()").extract_first()
            car_list_info['car_url'] = 'https://www.guazi.com' + car_item.xpath("./a/@href").extract_first()
            # print(car_list_info)
            car_list_info['item_type'] = 'car_info_item'
            yield scrapy.Request(url=car_list_info['car_url'], callback=self.handle_car_info, dont_filter=True, meta=car_list_info, errback=self.handle_err)

        if response.xpath("//ul[@class='pageLink clearfix']/li[last()]//span/text()").extract_first() == '下一页':
            value_search = re.compile("https://www.guazi.com/(.*?)/(.*?)/o(\d+)i7")
            value = value_search.findall(response.url)[0]
            response.request.meta['task_url'] = 'https://www.guazi.com/%s/%s/o%si7' % (value[0], value[1], str(int(value[2])+1))
            yield scrapy.Request(url=response.request.meta['task_url'], callback=self.handle_car_item, meta=response.request.meta, dont_filter=True, errback=self.handle_err)


    def handle_car_info(self, response):
        # print(response.text)
        car_id_search = re.compile(r"车源号：(.*?)\s+")
        car_info = GuaziScrapyProjectItem()
        car_info['car_id'] = car_id_search.search(response.text).group(1)
        car_info['car_name'] = response.request.meta['car_name']
        car_info['from_url'] = response.request.meta['car_url']
        car_info['car_price'] = response.xpath("//span[@class='price-num']/text()").extract_first().strip()
        # car_info['license_time'] = response.xpath("//ul[@class='assort clearfix']/li[@class='one']/span/text()").extract_first().strip()
        car_info['km_info'] = response.xpath("//ul[@class='assort clearfix']/li[@class='two']/span/text()").extract_first().strip()
        car_info['license_location'] = response.xpath("//ul[@class='assort clearfix']/li[@class='three']/span/text()").extract()[0].strip()
        # car_info['desplacement_info'] = response.xpath("//ul[@class='assort clearfix']/li[@class='three']/span/text()").extract()[1].strip()
        car_info['transmission_case'] = response.xpath("//ul[@class='assort clearfix']/li[@class='last']/span/text()").extract_first().strip()
        print(car_info)
        yield car_info