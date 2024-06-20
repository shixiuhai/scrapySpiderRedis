import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = "baiduSpider"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        
        self.logger.info("=====================")
        self.logger.info(response.text)
        self.logger.info("--------------------")