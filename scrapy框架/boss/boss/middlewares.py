# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
import json
import requests
from boss.models import ProxyModel
from twisted.internet.defer import DeferredLock


class UserAgentDownloadMiddleware(object):
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'
    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent


class IPProxyDowmloadMiddleware(object):
    PROXIES = [
        "http://178.44.170.152:8000",
        "http://110.44.113.183:8080",
        "http://209.126.124.73:8888",
        "http://84.42.79.243:8080",
        "http://209.126.124.73:9280"
    ]

    def __init__(self):
        super(IPProxyDowmloadMiddleware, self).__init__()
        self.current_proxy = None
        self.lock = DeferredLock()

    def process_request(self, request, spider):
        if 'proxy' not in request.meta or self.current_proxy.is_expring:
            self.update_proxy()
        request.meta['proxy'] = self.current_proxy.proxy
        proxy = random.choice(self.PROXIES)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        if response.status != 200 or "captcha" in response.url:
            if not self.current_proxy.blacked:
                self.current_proxy.blacked = True
            self.update_proxy()
            return request
        return response

    def update_proxy(self):
        self.lock.acquire()
        if not self.current_proxy or self.current_proxy.is_expring or self.current_proxy.blacked:
            response = requests.get(self.PROXIES)
            text = response.text
            result = json.loads(text)
            if len(result['data']) > 0:
                data = result['data'][0]
                proxy_model = ProxyModel(data)
                self.current_proxy = proxy_model
                # return proxy_model
        self.lock.release()
