import requests
from lxml import etree
import json
import  pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
myclient.admin.authenticate("admin", "123456")
mydb = myclient['db_51job']
mycollection = mydb['collection_51job']

url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
response = requests.get(url=url, headers=header)
response.encoding = 'gbk'

html_51job = etree.HTML(response.text)
all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
print(all_div)
info_list = []
for item in all_div:
    info = {}
    info['job_name'] = item.xpath("./p/span/a/@title")
    info['company_name'] = item.xpath(".//span[@class='t2']/a/@title")[0]
    info['company_address'] = item.xpath(".//span[@class='t3']/text()")[0]
    try:
        info['money'] = item.xpath(".//span[@class='t4']/text()")[0]
    except Exception as e:
        info['money'] = '无数据'
    info['date'] = item.xpath(".//span[@class='t5']/text()")[0]
    info_list.append(info)

mycollection.insert_many(info_list)
# print(json.dumps(info_list))