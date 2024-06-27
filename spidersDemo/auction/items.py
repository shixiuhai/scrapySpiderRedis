# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyspiderredisItem(scrapy.Item):
    """_summary_
    table 是表名
    =左边的字段就是mysql里表的字段,默认是intiCode里cwcwclothingSpider表
    Args:
        scrapy (_type_): _description_
    """
    # define the fields for your item here like:
    table="cwcwclothing"
    link=scrapy.Field()
    title=scrapy.Field()
    sort=scrapy.Field()
    num=scrapy.Field()
    price=scrapy.Field()
    size=scrapy.Field()
    color=scrapy.Field()
    color_img=scrapy.Field()
    intro=scrapy.Field()
    main_img=scrapy.Field()
    detail_img=scrapy.Field()
    sale=scrapy.Field()
    evaluate_num=scrapy.Field()
    mark=scrapy.Field()
    seo_title=scrapy.Field()
    seo_intro=scrapy.Field()
    seo_key=scrapy.Field()
    status=scrapy.Field()
    create_time=scrapy.Field()
    
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