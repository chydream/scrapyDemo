import re
import time

import requests
#
# # response = requests.get(url="http://httpbin.org/ip")
# response = requests.get(url="http://www.qq.com")
# print(response.text)

# data = {"name": "imooc"}
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)

# data = {'key1': 'value', 'key2': 'value2'}
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.url)
# print(response.text)
# print(response.headers)

# response = requests.get(url='https://www.imooc.com/static/img/index/logo.png')
#
# with open('imooc.png', 'wb') as f:
#     f.write(response.content)
# header = {
#     'user-agent': 'imooc/v1'
# }
# response = requests.get("http://httpbin.org/ip", headers=header, timeout=2)
# data = response.json()
# print(data)
# print(data['origin'])
# print(response.status_code)
# print(response.headers)
# print(response.request.headers)



# url = 'https://www.baidu.com'
# header = {
#     'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
# }
# response = requests.get(url=url, headers=header)
# print(response.cookies)

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='hello imooc')
# response = requests.get(url=url,cookies=cookies)
# print(response.text)


index_url = 'http://account.chinaunix.net/login'
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "account.chinaunix.net",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
}
login_session = requests.session()
token_search = re.compile(r'name="_token"\svalue="(.*?)"')
index_response = login_session.get(url=index_url, headers=header)
# print(index_response.text)
token_value = re.search(token_search, index_response.text).group(1)
print(token_value)
data = {
    "username":"tianyichy",
    "password":"chen0591",
    "_token": token_value,
    "_t":int(time.time())
}
login_url = 'http://account.chinaunix.net/login/login'
login_response = login_session.post(url=login_url, headers=header, data=data)
print(login_response.text)

phone_url = 'http://account.chinaunix.net/ucenter/user/index/'
phone_response = login_session.get(url=phone_url, headers=header)
print(phone_response.text)