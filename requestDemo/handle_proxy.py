import requests

proxy = {
    # "http": "http://117.69.168.173"
    "http":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
    "https":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
}

# url = 'http://httpbin/org/ip'
# for i in range(5):
#     response = requests.get(url=url, proxies=proxy)
#     print(response.text)

url = "https://requestb.in/"
response = requests.get(url=url, verify=False)  # verify='/path/to/certfile'
print(response.text)