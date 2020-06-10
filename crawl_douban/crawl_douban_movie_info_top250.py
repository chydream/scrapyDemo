import requests
from lxml import etree
from handle_mongo import douban_mongo
from concurrent.futures.thread import ThreadPoolExecutor

class HandleDoubanMovieTop250(object):
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        self.page_url = []

    def handle_page_url(self):
        index_url = 'https://movie.douban.com/top250?start=0&filter='
        response = requests.get(url=index_url, headers=self.header, timeout=2)
        html = etree.HTML(response.text)
        page_total = int(html.xpath("//div[@class='paginator']/a[last()]/text()")[0]) + 1
        for i in range(1, page_total):
            url = 'https://movie.douban.com/top250?start={}&filter='.format(25*(i-1))
            self.page_url.append(url)

    def handle_request(self):
        self.handle_page_url()
        for url in self.page_url:
            response = requests.get(url=url, headers=self.header, timeout=2)
            html = etree.HTML(response.text)
            url_list = html.xpath('//div[@class="hd"]/a/@href')
            for url_item in url_list:
                print(url_item)
                self.handle_page_detail(url_item, url)


    def handle_page_detail(self, url, from_url):
        response = requests.get(url=url, headers=self.header, timeout=2)
        html = etree.HTML(response.text)
        movice_info = {}
        movice_info['movie_name'] = html.xpath('//div[@id="content"]/h1/span[1]/text()')[0]  # 电影名称
        movice_info['actors_information'] = (',').join(html.xpath('//span[@class="actor"]/span/a/text()'))  # 电影演职人员信息
        movice_info['score'] = html.xpath('//div[@class="rating_self clearfix"]/strong/text()')  # 电影评分数值
        movice_info['evaluate'] = html.xpath('//div[@class="rating_sum"]/a/span/text()')[0]  # 评价数信息
        movice_info['describe'] = html.xpath('//span[@property="v:summary"]/text()')[0].strip()  # 电影简述信息
        movice_info['from_url'] = from_url  # 来源URL信息
        douban_mongo.handle_save_data(movice_info)

    def run(self):
        executor = ThreadPoolExecutor()
        task1 = executor.submit(self.handle_request)
        executor.shutdown()

def main():
    douban = HandleDoubanMovieTop250()
    douban.run()



if __name__ == '__main__':
    main()
