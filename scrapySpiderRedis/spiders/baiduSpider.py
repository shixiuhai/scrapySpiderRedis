import scrapy
# from scrapy_redis.spiders import RedisSpider
from scrapySpiderRedis.items import ScrapyspiderredisItem


class BaiduspiderSpider(scrapy.Spider):
    name = "baiduSpider"
    allowed_domains = ["baidu.com","bing.com"]
    start_urls = ["https://www.baidu.com","https://www.bing.com"]

    def parse(self, response):
        # response.text 
        self.logger.info("=====================")
        # self.logger.info(response.text)
        self.logger.info("--------------------")
        # yield scrapy.Request("https://www.baidu.com", callback=self.parse)
        # yield {
        #     'url': response.url,
        #     'content_length': len(response.body)
        # }
        item=ScrapyspiderredisItem()
        item["link"]="http://127.0"
        item["title"]="你好"
        yield item
        