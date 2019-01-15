# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector, Request


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']

    def start_requests(self):
        start_urls = ['https://www.jd.com/allSort.aspx', ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_category)

    def parse(self, response):
        item = response.css("div.items")
        # for title in item.css("dl.clearfix"):
        # print(title.extract())
        # print(title.css("dt a::text").extract_first() + ":" + title.css("dt a::attr(href)").extract_first())
        # print(title.css("dt").extract())
        #     yield Request(url="https:" + title.css("dt a::attr(href)").extract_first(), callback=self.parse_list)
        yield Request(url="https://e.jd.com/ebook.html", callback=self.parse_list)

    def parse_list(self, response):
        for url in response.css('a'):
            result = url.css("a::attr(href)").extract_first()
            if 'https' not in result and 'http' not in result and 'javascript' not in result:
                # print(result)
                yield Request(url="https:" + result, callback=self.parse_detail)

    def parse_detail(self, response):
        # print(response.body)
        id = response.url.split("/")[-1].split('.')[0]
        title = response.css("div.sku-name::text").extract_first()
        author = response.css("div.author a::text").extract_first()

        # price_id = "price J-p-"+id
        # price = response.css("//span[@class='"+price_id+"']").extract()
        if title is not None and author is not None:
            print(title)
            print(author)
            print(response.css("div.comment-item").extract_first())

    def parse_category(self, response):
        """获取分类页"""
        selector = Selector(response)
        try:
            texts = selector.xpath(
                '//div[@class="category-item m"]/div[@class="mc"]/div[@class="items"]/dl/dd/a').extract()
            for text in texts:
                items = re.findall(r'<a href="(.*?)" target="_blank">(.*?)</a>', text)
                for item in items:
                    if item[0].split('.')[0][2:] != 'list':
                        yield Request(url='https:' + item[0], callback=self.parse_category)
                    else:
                        yield Request(url='https:' + item[0], callback=self.parse_list)
        except Exception as e:
            print('error:', e)

    def parse_list(self, response):
        """分别获得商品的地址和下一页地址"""
        meta = dict()
        meta['category'] = response.url.split('=')[1].split('&')[0]

        selector = Selector(response)
        texts = selector.xpath('//*[@id="plist"]/ul/li/div/div[@class="p-img"]/a').extract()
        for text in texts:
            items = re.findall(r'<a target="_blank" href="(.*?)">', text)
            yield Request(url='https:' + items[0], callback=self.parse_product, meta=meta)

    def parse_product(self,response):
        pass