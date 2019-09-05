# -*- coding: utf-8 -*-
import scrapy


class DoubanbookSpiderSpider(scrapy.Spider):
    name = 'doubanbook_spider'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
