import re

import requests
import execjs
from handle_mongo import mongo

url = 'https://www.guazi.com/www/buy'
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.guazi.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}

response = requests.get(url=url, headers=header)
response.encoding = 'utf-8'
# print(response.text)
# print(response.status_code)
if '正在打开中,请稍后' in response.text:
    value_search = re.compile(r"anti\('(.*?)','(.*?)'\)")
    string = value_search.search(response.text).group(1)
    key = value_search.search(response.text).group(2)
    # print(string, key)
    with open('guazi.js', 'r') as f:
        f_read = f.read()
    js = execjs.compile(f_read)
    js_return = js.call('anti', string, key)
    # print(js_return)
    cookie_value = 'antipas=' + js_return
    header['Cookie'] = cookie_value
    # print(header)
    response_send = requests.get(url=url, headers=header)
    # print(response_send.text)
    city_search = re.compile(r'href="\/(.*?)\/buy"\stitle=".*?">(.*?)\s*</a>')
    brand_search = re.compile(r'href="\/www\/(.*?)\/c-1/#bread"\s+>(.*?)</a>')
    city_list = city_search.findall(response_send.text)
    brand_list = brand_search.findall(response_send.text)
    print(city_list)
    # print(brand_list)
    for city in city_list:
        if city[1] == '北京':
            for brand in brand_list:
                info = {}
                info['task_url'] = 'https://www.guazi.com/' + city[0] + '/' + brand[0] + '/' + 'o1i7'
                info['city_name'] = city[1]
                info['brand_name'] = brand[1]
                print(info)
                info['item_type'] = 'list_item'
                mongo.save_task('guazi_task', info)