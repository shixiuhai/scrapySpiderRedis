# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyspiderredisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
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