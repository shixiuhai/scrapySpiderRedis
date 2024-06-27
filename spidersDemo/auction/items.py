# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
    
class AuctionSpiderItem(scrapy.Item):
    """_summary_
    数字拍卖实体类
    Args:
        scrapy (_type_): _description_
    """
    table = "auction_item"
    item_title = scrapy.Field()       # 拍品信息
    artist = scrapy.Field()           # 作者
    category = scrapy.Field()         # 拍品分类
    creation_year = scrapy.Field()    # 创作年代
    dimensions = scrapy.Field()       # 尺寸
    estimate = scrapy.Field()         # 估价
    price_sold = scrapy.Field()       # 成交价
    auction_date = scrapy.Field()     # 拍卖日期（字符串）
    auction_company = scrapy.Field()  # 拍卖公司
    auction_session = scrapy.Field()  # 拍卖专场
    auction_event = scrapy.Field()    # 拍卖会
    material = scrapy.Field()         # 材质
    inscription = scrapy.Field()      # 题识
    literature = scrapy.Field()       # 著录
    description = scrapy.Field()      # 拍品描述
    img_url = scrapy.Field()  # 图片url