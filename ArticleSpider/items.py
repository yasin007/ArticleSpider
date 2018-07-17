# 设置数据存储模板，用于结构化数据，如：Django的Mode
import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
