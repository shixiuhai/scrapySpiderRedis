# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyspiderredisItem(scrapy.Item):
    """_summary_
    table 是表名
    =左边的字段就是mysql里表的字段
    Args:
        scrapy (_type_): _description_
    """
    # define the fields for your item here like:
    table="demo"
    field_one=scrapy.Field()
    field_two=scrapy.Field()
    
class LvItem(scrapy.Item):
    table="ly"
    departure_place=scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    detail_url=scrapy.Field()
    tourist_spots=scrapy.Field()
    destination_place=scrapy.Field()
    destination_place1=scrapy.Field()
    day_number=scrapy.Field()
    tourist_spots_number=scrapy.Field()
