# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse


class JoboboleSpider(scrapy.Spider):
    name = 'jobobole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1.获取文章列表页中的url并交给scrapy并进行解析
        2.获取下一页的url 并交给scrapy进行下载,下载完成后交给parse参数
        :param response:
        :return:
        """
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": ""},
                          callback=self.parse_detail)

        # 获取下一页的url 并交给scrapy进行下载,下载完成后交给parse参数
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")
        print(next_urls)
        if next_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)

    def parse_detail(self, response):
        # 提取文字的具体字段
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_data = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("·",
                                                                                                                    "").strip()
        praise_nums = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract()[0]
        fav_nums = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_nums = response.xpath('//a[@href="#article-comment"]/span').extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)

        content = response.xpath("//div[@class='entry']").extract()[0]
        pass
