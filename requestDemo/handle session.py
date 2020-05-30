import re

import requests

class Login(object):
    def __init__(self):
        self.request_session = requests.session()
        self.header ={
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        }
        self.csrf_value = ''

    def handle_csrf_token(self):
        self.index_url = 'http://flask.zhaedu.com/mall/product/list/1'
        csrf_response = self.request_session.get(url=self.index_url, headers=self.header)
        csrf_search = re.compile(r'name="csrf_token"\stype="hidden"\svalue="(.*?)">')
        self.csrf_value = csrf_search.search(csrf_response.text).group(1)
        print(self.csrf_value)

    def handle_login(self):
        self.handle_csrf_token()
        username = input("请输入用户名")
        password = input("请输入密码")
        login_url = "http://flask.zhaedu.com/accounts/login"
        data = {
            "csrf_token": self.csrf_value,
            "username": username,
            "password": password
        }
        self.request_session.post(url=login_url, headers=self.header, data=data)
        response = self.request_session.get(url=self.index_url,headers=self.header)
        print(response.text)

if __name__ == '__main__':
    flask_login = Login()
    flask_login.handle_login()