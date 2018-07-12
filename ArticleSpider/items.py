# 设置数据存储模板，用于结构化数据，如：Django的Mode
import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticItem(scrapy.Item):
    title = scrapy.Field()
    create_data = scrapy.Field()
    url = scrapy.Field()
