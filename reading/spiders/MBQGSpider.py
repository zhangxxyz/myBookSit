
import scrapy
from reading.spiders.MBQG import MBGSearch

class myMBGQSpider(scrapy.Spider):
    name = 'myMBQG'
    def __init__(self,searchName=None,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.start_urls = [MBGSearch.getUrl(searchName)]

    def parse(self, response):
        print('成功',response.text)
        # bookType = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s1"]/text()').extract()[0]
        bookName = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s2"]/a/text()').extract()[0].strip()
        # lastZhangjie = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s3"]/a/text()').extract()[0]
        # writer = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s4"]/text()').extract()[0]
        # updateTime = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s6"]/text()').extract()[0]
        # updateStatus = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s7"]/text()').extract()[0]
        bookUrl = response.xpath('.//div[@class = "search-list"]/ul/li/span[@class = "s2"]//@href').extract()
        print(bookUrl,bookName)
        yield scrapy.Request(bookUrl,callback=self.getBookInfo)

    def getBookInfo(self,response):
        pass


