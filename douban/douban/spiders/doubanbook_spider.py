# -*- coding: utf-8 -*-
import scrapy


class DoubanbookSpiderSpider(scrapy.Spider):
    name = 'doubanbook_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4']

    # 获得所有目录页
    def parse(self, response):
        page_count = response.xpath('//div[@class="paginator"]/a/text()').extract()[-1]
        # for page_num in range(1, int(page_count)):
        for page_num in range(1, 2):
            full_cattle_url = response.url + '?start=' + str(page_num)
            print(full_cattle_url)
            yield scrapy.Request(url=full_cattle_url, callback=self.parse_catlle)

    # 获得目录页所有链接
    def parse_catlle(self, response):
        print(response.url)
        url_list = response.xpath('//div[@class="info"]/h2/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        pass