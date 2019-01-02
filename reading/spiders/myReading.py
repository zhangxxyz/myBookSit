# -*- coding: utf-8 -*-
import scrapy
import reading.spiders.biQuGe as BQG  #笔趣阁
from lxml import  etree
from fake_useragent import UserAgent
import faker.providers.user_agent
import reading.items as Item
import js2py
import reading.utils.enumUtils as myEnum

class MyreadingSpider(scrapy.Spider):
    name = 'myReading'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        array = BQG.getUrl()
        for i in array:
            yield scrapy.Request(i,callback=self.BQGContent)
        pass


    def BQGContent(self,resp):
        if resp.status == 521:
            print(resp.text)
            print('解码js')
            jsStr = str(resp.text).split('<script>')[1]
            jsStr = jsStr.split('</script>')[0]
            print(jsStr)
            data = js2py.eval_js(jsStr)
            print(data.execute('你好'))
            print(data,'js执行结果')
            return
        # content=etree.HTML(resp.text)
        # print(content)
        # print('成功')
        # print(resp.meta)
        if resp.status != 200:
            print('爬取失败', resp.url, resp.status)
            return
        title  = resp.xpath('.//div[@class = "box_con"]//h1/text()').extract()[0]
        book   = resp.xpath('.//div[@class = "box_con"]/div/div//p/text()').extract()
        updatTime = ''
        writer = ''
        for i in book:
            writer = str(book[0]).split('：')[-1]
            timeLoc = str(i).find('最后更新：')
            if timeLoc != -1:
                updatTime = str(i)[5:].strip()
        bookInfo = book[-1]
        sectionUrl = resp.xpath('.//div[@class = "box_con"]/div//dd/a/@href').extract()
        sectionTitl = resp.xpath('.//div[@class = "box_con"]/div//dd/a/text()').extract()
        item =  Item.bookInfoItem()
        item['writer'] = writer
        item['title'] = title
        item['updatTime'] = updatTime
        item['bookInfo'] = bookInfo
        item['url'] = resp.url
        item['identify'] = myEnum.itemEnum.BQGBookInfo

        yield item
        for i in sectionUrl:
            url = '{}{}'.format(BQG.biqugeUrl,i)
            # print(url)
        yield  scrapy.Request(url,callback=self.BQGDetailContent)


    def BQGDetailContent(self,resp):
        print(type(resp.status),resp.url,resp.status)

        print('这里')

        item = Item.bookContent()
        item['url'] = resp.url
        if resp.status != 200:
            print('爬取失败',resp.url,resp.status)
            item['identify'] = myEnum.itemEnum.BQGBookCententFail
            yield item
            return

        item['title'] = resp.xpath('.//div[@class = "content_read"]//div[@class = "bookname"]/h1/text()').extract()[0]
        item['bookName'] = resp.xpath('.//div[@class = "content_read"]/div[@class = "box_con"]//div[@class = "bottem1"]/a/text()').extract()[2]
        content = resp.xpath('.//div[@class = "content_read"]/div/div[@id = "content"]/text()').extract()
        text = ""
        for i in content:
            text = '{}{}'.format(text,str(i))
        item['content'] = text



        indexStr = str(resp.url).split('/')[-1]
        index = indexStr[0:-5]
        item['index'] = index
        item['identify'] = myEnum.itemEnum.BQGBookContent
        yield item


#  完结  更新状态  太监  三个库
#  多个源的爬取配置
#  代理ip 多UA  延迟爬取 云打码


