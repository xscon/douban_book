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

    def get_insert_sql_and_data(self):
        insert = 'INSERT INTO douban_book(title,img_url,author,year,page_count,price,url,score,content) ' \
                 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['title'],self['img_url'],self['author'],self['year'],self['page_count'],self['price'],self['url'],self['score'],self['content'])
        return (insert, data)