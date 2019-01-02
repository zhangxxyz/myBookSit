# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
from .ipFile import ipArray
import random
import time
import hashlib
import sys



class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random') #从setting文件中读取RANDOM_UA_TYPE值

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        user_agent_random=get_ua()
        # randomUa["User-Agent"] = user_agent_random
        # request.headers = randomUa
        # print(request.headers)
        request.headers.setdefault('User-Agent', user_agent_random)
        # print(request.headers, 'head查询')


class RandomProxyMiddleware(object):
    def __init__(self):
        secret = '0821dafd74594ce9ab2ad9d78db69e73'
        orderNo = 'ZF201812218554QCqk8V'
        ip_port = "forward.xdaili.cn:80"
        timeStamp = str(int(time.time()))
        useInformation = "orderno={},secret={},timestamp={}".format(orderNo,secret,timeStamp)
        print(useInformation)
        string = useInformation.encode()
        md5Str = hashlib.md5(string)
        x = md5Str.hexdigest()  # 16进制
        sign = x.upper()           # 转成大写
        self.proxy = "http://" + ip_port
        self.auth = "sign={}&orderno={}&timestamp={}".format(sign,orderNo,timeStamp)

    '''动态设置ip代理'''
    def process_request(self,request,spider):
        # index = random.randint(0,len(ipArray)-1)
        # print(ipArray[index])
        # request.meta["proxy"] = ipArray[index]

        request.meta["proxy"] = self.proxy
        request.headers.setdefault('Proxy-Authorization', self.auth)
        # print(request.meta,'ip设置')

        pass



class ReadingSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ReadingDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        print(request,99999)
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        if response.status == 200:
            return  response
        else:
            return request
        # return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
