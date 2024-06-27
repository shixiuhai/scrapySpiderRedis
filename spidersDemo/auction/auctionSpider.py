from typing import Iterable
import scrapy
from scrapy import Request
from scrapySpiderRedis.log import Logging
from gerapyPlaywright import PlaywrightRequest
from scrapySpiderRedis.items import AuctionSpiderItem
from scrapy.http import HtmlResponse

class AuctionspiderSpider(scrapy.Spider):
    name = "auctionSpider"
    allowed_domains = ["auction.artron.net"]
    # start_urls = ["https://auction.artron.net"]
    start_url = "https://auction.artron.net/preauction/pmp?status=2&page=1&orderby=2&evaluation_price=&advancedSeach=&startdate=&enddate=&rmbPriceStart=&rmbPriceEnd=&classCode=&organCode=&city=&organName=&item=&is_total=1&keyword="
    logger = Logging("baiduSpiderByPlaywright.log").get_logger() # 使用自定义日志器

    def start_requests(self) -> Iterable[Request]:
        yield PlaywrightRequest(url=self.start_url,callback=self.parse_artist,meta={"page":1},browser_type="webkit")
        
    def parse_artist(self,response:HtmlResponse)->Iterable[Request]:
                                                # //*[@id="app"]/div/div[7]/div[2]/dl[2]/dt/a
        artist_detail_url_list = ["https://" + self.allowed_domains[0]+item for item in response.xpath('//*[@id="app"]/div/div[7]/div[2]/dl/dt/a/@href').extract()]
        for artist_detail_url in  artist_detail_url_list:
            yield PlaywrightRequest(url=artist_detail_url,callback=self.parse_artist_detail)
        next_page = response.meta["page"] + 1
        yield PlaywrightRequest(url=self.start_url.replace("page=1",f"page={next_page}"),callback=self.parse_artist,meta={"page":next_page})

    def parse_artist_detail(self,response:HtmlResponse)->Iterable[Request]:
        # self.logger.info(f"正在解析藏品页：{response.url}")
        item = AuctionSpiderItem(
            
            # artist = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[2]/dd/a').get(),
           
            # creation_year = scrapy.Field()    # 创作年代

            # price_sold = scrapy.Field()       # 成交价

    
            # inscription = scrapy.Field()      # 题识
            # literature = scrapy.Field()       # 著录
            # description = scrapy.Field()      # 拍品描述
            
        )
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[1]/dd/text()').get() is not None:
            item["item_title"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[1]/dd/text()').get()
        
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[2]/dd/a/text()').get() is not None:
            item["category"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[2]/dd/a/text()').get()
        
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[4]/dd/span/text()').get() is not None:
            item["dimensions"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[4]/dd/span/text()').get()
        
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[5]/dd/text()').get() is not None:
            item["estimate"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[1]/dl[5]/dd/text()').get()
        
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[1]/dd/text()').get() is not None:
            item["auction_date"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[1]/dd/text()').get()
        
        # item["material"] = response.xpath("/abc").get()

        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[2]/dd/a/text()').get() is not None:
            item["auction_company"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[2]/dd/a/text()').get().strip()

        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[3]/dd/a/text()').get() is not None:
            item["auction_session"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[3]/dd/a/text()').get().strip()
            
        if response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[4]/dd/a/text()').get() is not None:
            item["auction_event"] = response.xpath('//*[@id="app"]/div/div[5]/div[5]/div[1]/div[1]/div/div[2]/dl[4]/dd/a/text()').get().strip()
        if response.xpath('//*[@id="smallPic"]/@src').get() is not None: 
            item["img_url"] = response.xpath('//*[@id="smallPic"]/@src').get()
        yield item