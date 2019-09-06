# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douban.mysqlhelper import MysqlHelper

class DoubanPipeline(object):

    def process_item(self, item, spider):
        return item


class Mysqlhelper(object):
    def __init__(self):
        self.helper = MysqlHelper()

    def process_item(self, item, spider):
        (insert, data) = item.get_insert_sql_and_data()
        self.helper.execute_modify_sql(insert, data)
        return item

