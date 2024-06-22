import scrapy
# from scrapy_redis.spiders import RedisSpider
from scrapySpiderRedis.items import ScrapyspiderredisItem
from scrapySpiderRedis.log import Logging

class BaiduspiderSpider(scrapy.Spider):
    name = "baiduSpider"
    allowed_domains = ["baidu.com","bing.com"]
    start_urls = ["https://www.baidu.com","https://www.bing.com"]
    logger = Logging("cwcwclothingSpider.log").get_logger() # 使用自定义日志器
    
    # def __init__(self, *args, **kwargs):
    #     super(BaiduspiderSpider, self).__init__(*args, **kwargs)
    #     # 定义实例变量 logger
    #     self.logger = Logging("baiduSpider.log").get_logger()

    def parse(self, response):
        self.logger.info(response.text)
        # yield scrapy.Request("https://www.baidu.com", callback=self.parse)
        # yield {
        #     'url': response.url,
        #     'content_length': len(response.body)
        # }
        item=ScrapyspiderredisItem()
        item["link"]="http://127.0"
        item["title"]="你好"
        yield item
        