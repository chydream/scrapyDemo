import requests
from multiprocessing import Queue
from lxml import etree
import threading
from study_crawl_job.handle_mongo import insert_data

class Crawl_page(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(Crawl_page, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        self.proxy = {
            # "http": "http://117.69.168.173"
            "http":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
            "https":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
        }

    def run(self):
        print('当前启动的处理页码的任务为%s' % self.thread_name)
        while not page_flag:
            try:
                page = self.page_queue.get(block=False)
                page_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,' + str(page) + '.html'
                print('当前构造的url为%s'% page_url)
                response = requests.get(url=page_url, headers = self.header)
                response.encoding = 'gbk'
                self.data_queue.put(response.text)
            except Exception as e:
                pass

class Crawl_html(threading.Thread):
    def __init__(self, thread_name, data_queue, lock):
        super(Crawl_html,self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        print('当前启动的处理文本任务线程为%s' % self.thread_name)
        while not data_flag:
            try:
                text = self.data_queue.get(block = False)
                result = self.parse(text)
                with self.lock:
                    insert_data.insert_db(result)
            except Exception as e:
                pass

    def parse(self, text):
        html_51job = etree.HTML(text)
        all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
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
        return info_list


page_flag = False
data_flag = False

def main():
    page_queue = Queue()
    data_queue = Queue()

    lock = threading.Lock()

    for page in range(1, 736):
        page_queue.put(page)

    print("当前页码队列的总量为%s"%page_queue.qsize())

    crawl_page_list = ["页码处理线程1号", "页码处理线程2号", "页码处理线程3号"]
    page_thread_list = []
    for thread_name_page in crawl_page_list:
        thread_page = Crawl_page(thread_name_page, page_queue, data_queue)
        thread_page.start()
        page_thread_list.append(thread_page)

    parseList = ["文本处理线程1号", "文本处理线程2号", "文本处理线程3号"]
    parse_thread_list = []
    for thread_name_parse in parseList:
        thread_parse = Crawl_html(thread_name_page, data_queue, lock)
        thread_parse.start()
        parse_thread_list.append(thread_parse)

    global page_flag
    while not page_queue.empty():
        pass
    page_flag = True

    for thread_page_join in page_thread_list:
        thread_page_join.join()
        print(thread_page_join.thread_name, '处理结束')

    global data_flag
    while not data_queue.empty():
        pass
    data_flag = True

    for thread_parse_join in parse_thread_list:
        thread_parse_join.join()
        print(thread_parse_join.thread_name, '处理结束')

if __name__ == '__main__':
    main()