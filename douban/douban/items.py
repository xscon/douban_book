# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    img_url = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    page_count = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    content = scrapy.Field()

