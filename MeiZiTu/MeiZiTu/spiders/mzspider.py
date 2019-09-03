# -*- coding: utf-8 -*-
import scrapy


class MzspiderSpider(scrapy.Spider):
    name = 'mzspider'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    def parse(self, response):
        pass
