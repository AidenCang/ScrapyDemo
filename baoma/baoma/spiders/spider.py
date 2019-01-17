# -*- coding: utf-8 -*-
import scrapy
from ..items import BaomaItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        # SelecorList类型
        uiboxs = response.xpath('//div[@class = "uibox"]')[1:]  # 第一个我们不需要
        for uibox in uiboxs:
            catagory = uibox.xpath('.//div[@class = "uibox-title"]/a/text()').get()
            urls = uibox.xpath('.//ul/li/a/img/@src').getall()
            # 遍历列表，并将列表中的某一项执行函数操作，再将函数的返回值以列表的形式返回
            # map()
            # for url in urls:
            #     # url = 'https:' + url
            #     # print(url)
            #     #方法二：
            #     url = response.urljoin(url)
            #     print(url)
            # 方法三：
            # 将列表中的每一项进行遍历传递给lambda表达式，并执行函数中的代码，再以返回值以列表形式进行返回,结果是map对象，接着使用list转换为列表
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = BaomaItem(catagory=catagory, urls=urls)
            yield item
