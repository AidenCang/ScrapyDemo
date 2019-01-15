# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import TencentItem


class TencentcrawlSpider(CrawlSpider):
    name = 'tencentcrawl'
    allow_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink, callback="parseTencent", follow=True)
    ]

    # rules = (
    #     # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
    #     Rule(pagelink, callback="parseTencent", follow=True)
    #     # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # 指定的回调函数
    def parseTencent(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionLike'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workloaction'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
