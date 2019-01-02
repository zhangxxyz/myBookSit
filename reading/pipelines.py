# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from reading.utils.mysqlUtils import my_sql
import reading.utils.enumUtils as myEnum

class ReadingPipeline(object):
    def __init__(self):
        print('开始init')
    def process_item(self, item, spider):
        # print(dict(item))
        itemDict = dict(item)
        itemType = itemDict.get('identify',"0")
        if itemType == myEnum.itemEnum.BQGBookInfo:
            sql = "insert into mybooks(bookName,writer,info,updateTime,url) values('%s','%s','%s','%s','%s')"%(str(itemDict.get('title',"暂无")),str(itemDict.get('writer',"暂无")),str(itemDict.get('bookInfo',"暂无")),str(itemDict.get('updatTime',"暂无")),str(itemDict.get('url',"暂无")))
            self._insert(sql)

        if itemType == myEnum.itemEnum.BQGBookContent:
            sql = "insert into textContent(bookName,content,contentIndex,title,url) values('%s','%s','%d','%s','%s')"%(str(itemDict.get('bookName',"0")),str(itemDict.get('content',"暂无")),int(itemDict.get('index','0')),str(itemDict.get('title',"暂无")),str(itemDict.get('url',"暂无")))
            self._insert(sql)

        if itemType == myEnum.itemEnum.BQGBookCententFail:
            sql = "insert into BQGfailUrl(url) values(itemDict.get('url','暂无'))"
            self._insert(sql)

            pass

        return item

    def open_spider(self,spider):
        print('开始打开')
        pass

    def close_spider(self,spider):

        pass

    def _insert(self,sql):
        mysql = my_sql()
        mysql.insert(sql)