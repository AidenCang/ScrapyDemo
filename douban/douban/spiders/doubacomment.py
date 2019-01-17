# -*- coding: utf-8 -*-
import scrapy


class DoubacommentSpider(scrapy.Spider):
    name = 'doubacomment'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        pass
