from typing import Iterable
import scrapy
from scrapy import Request
# from scrapy_redis.spiders import RedisSpider
from scrapySpiderRedis.items import ScrapyspiderredisItem
from scrapySpiderRedis.log import Logging
from gerapySelenium import SeleniumRequest
from scrapy.http import HtmlResponse


class baiduSpiderBySelenium(scrapy.Spider):
    name = "baiduSpiderBySelenium"
    allowed_domains = ["baidu.com","bing.com"]
    # start_urls = ["https://www.baidu.com","https://www.bing.com"]
    start_url="https://www.baidu.com"
    logger = Logging("baiduSpiderBySelenium.log").get_logger() # 使用自定义日志器
    
    # def __init__(self, *args, **kwargs):
    #     super(BaiduspiderSpider, self).__init__(*args, **kwargs)
    #     # 定义实例变量 logger
    #     self.logger = Logging("baiduSpider.log").get_logger()
    def start_requests(self) -> Iterable[Request]:
        # 默认 priority=0.5 数值越高，优先级越大,范围 0 到 1
        yield SeleniumRequest(url=self.start_url,callback=self.parse)

    def parse(self, response:HtmlResponse):
        self.logger.info(response.text[0:100])
        # yield scrapy.Request("https://www.baidu.com", callback=self.parse)
        # yield {
        #     'url': response.url,
        #     'content_length': len(response.body)
        # }
        # item=ScrapyspiderredisItem()
        # item["link"]="http://127.0"
        # item["title"]="你好"
        # yield item
        