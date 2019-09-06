# -*- coding: utf-8 -*-
import scrapy
import re
from douban.items import DoubanItem


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
            yield scrapy.Request(url=full_cattle_url, callback=self.parse_catlle)

    # 获得目录页所有链接
    def parse_catlle(self, response):
        url_list = response.xpath('//div[@class="info"]/h2/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        title = response.xpath('//h1/span/text()').extract_first()
        img_url = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()
        author = re.search(r'<span class="pl">出版社:</span> (.*?)<br/>', response.text).group(1)
        year = re.search(r'<span class="pl">出版年:</span> (.*?)<br/>', response.text).group(1)
        page_count = re.search(r'<span class="pl">页数:</span> (.*?)<br/>', response.text).group(1)
        price = re.search(r'<span class="pl">定价:</span> (.*?)<br/>', response.text).group(1)
        url = response.url
        score = re.search(r'rating_num " property="v:average"> (.*?) </strong>', response.text).group(1)
        content = '.'.join(response.xpath('//div[@class="intro"]/p[1]/text()').extract())
        item = DoubanItem()
        item['title'] = title
        item['img_url'] = img_url
        item['author'] = author
        item['year'] = year
        item['page_count'] = page_count
        item['price'] = price
        item['url'] = url
        item['score'] = score
        item['content'] = content
        yield item




