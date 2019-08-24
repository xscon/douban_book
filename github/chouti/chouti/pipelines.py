# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ChoutiPipeline(object):
    def open_spider(self, spider):
        self.f = open("chouti.txt", "a", encoding="utf-8")

    def process_item(self, item, spider):
        info = item["title"] + ":" + item["url"]+ "\n"
        self.f.write(info)
        self.f.flush()

    def close_spider(self, spider):
        self.f.close()