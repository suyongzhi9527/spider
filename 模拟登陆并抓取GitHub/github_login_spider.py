import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'Host': 'github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div[@id="login"]//input[1]/@value')[0]
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[@class="news"]//text()')
        # print(dynamics)
        # for item in dynamics:
        #     dynamic = item.xpath('.//div[contains(@class, "f4")]/text()')
        #     print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        bio = selector.xpath('//textarea[@id="user_profile_bio"]/text()')[0]
        print(name, bio)


if __name__ == '__main__':
    git = Login()
    git.login(email='1125699801@qq.com', password='1125699801syz')
