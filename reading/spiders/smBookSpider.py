import scrapy
from reading.spiders.SMBook import search


class mySMBook(scrapy.Spider):
    name = "mySM"
    print('执行了神马爬虫')

    def __init__(self, searchName=None, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.start_urls = [search.getSearchURl(searchName)]







    def parse(self, response):
        print('神马的响应')

        if response.status != 200:
            return

        url = response.xpath('.//div[@class = "article ali_row"]/h2/a/@href').extract()
        print(url)
        print('响应内容')

        print(response.text)


