# -*- coding: utf-8 -*-
import scrapy

from ..items import TencentItem


class TencentpostionSpider(scrapy.Spider):
    name = 'tencentPostion'
    allowed_domains = ['tencent.com']
    # start_urls = ['http://tencent.com/']
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['positionname'] = each.xpath("./td[1]/a/text()").extract_first()
            item['positionLike'] = each.xpath("./td[1]/a/@href").extract_first()
            item['positionType'] = each.xpath("./td[2]/text()").extract_first()
            item['peopleNum'] = each.xpath("./td[3]/text()").extract_first()
            item['workloaction'] = each.xpath("./td[4]/text()").extract_first()
            item['publishTime'] = each.xpath("./td[5]/text()").extract_first()
            yield item

        if self.offset < 2805:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
