# -*- coding: utf-8 -*-
import scrapy


class JoboboleSpider(scrapy.Spider):
    name = 'jobobole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        # /html/body/div[3]/div[3]/div[1]

        re_Selector = response.xpath('//*[@id="post-114185"]/div[1]/h1')
        pass
