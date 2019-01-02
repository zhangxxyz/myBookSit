# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class bookInfoItem(scrapy.Item):
    # 书的名字
    title = scrapy.Field()
    # 书籍最后更新时间
    updatTime = scrapy.Field()
    # 作者
    writer = scrapy.Field()
    # 书籍简介
    bookInfo = scrapy.Field()
    # 书籍url
    url = scrapy.Field()
    # 标识符 判断是书籍详情
    identify = scrapy.Field()

    pass

class bookContent(scrapy.Item):
    # 章节的序列
    index = scrapy.Field()
    # 章节标题
    title = scrapy.Field()
    # 章节内容
    content = scrapy.Field()
    # 书名
    bookName = scrapy.Field()
    # 章节url
    url    = scrapy.Field()
    # 是章节标示
    identify = scrapy.Field()



class ReadingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
