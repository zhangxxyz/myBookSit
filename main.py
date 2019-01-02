from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.cmdline import execute
# if __name__ == '__main__':


    # process = CrawlerProcess(get_project_settings())
    # process.crawl('myReading')
    # process.crawl('mySM')
    # process.start()


execute("scrapy crawl myReading".split())
# execute("scrapy crawl myMBQG -a searchName=圣墟".split())
