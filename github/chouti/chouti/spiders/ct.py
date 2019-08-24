# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.dupefilters import RFPDupeFilter
from ..items import ChoutiItem
from scrapy.http.cookies import CookieJar


class CtSpider(scrapy.Spider):
    name = 'ct'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com/all/hot/recent/1']
    cookie = None   # 设置初始值

    def parse(self, response):
        cookie_obj = CookieJar()
        cookie_obj.extract_cookies(response,response.request)
        self.cookie = cookie_obj._cookies  # 将捕获的cookie赋值给cookie
        yield Request(
            url="https://dig.chouti.com/login",
            method="POST",
            body="phone=8618938685515&password=avvcd123&oneMonth=1",  # DATA提交内容
            headers={"Content-Type":'application/x-www-form-urlencoded; charset=UTF-8'},  # POST方式，有要写
            callback=self.check_login
        )

    def check_login(self, response):
        print(response.text)
        yield Request(url='https://dig.chouti.com/', callback=self.good)

    def good(self, response):
        html_finder_obj = Selector(response=response)
        good_finder = html_finder_obj.xpath('//div[@share-linkid]/@share-linkid').extract()
        for good in good_finder:
            full_good_link = "https://dig.chouti.com/link/vote?linksId={}".format(good)
            yield Request(url=full_good_link, method='POST', cookies=self.cookie, callback=self.show_good)

        next_page_list_finder = html_finder_obj.xpath('//a[@class="ct_pagepa"]/@href').extract()
        for next_page_finder in next_page_list_finder:
            full_next_url = "https://dig.chouti.com" + next_page_finder
            rgs = Request(url=full_next_url, method='GET', callback=self.good, cookies=self.cookie)
            yield rgs

    def show_good(self, response):
        print(response.text)