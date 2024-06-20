import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = "baiduSpider"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass
