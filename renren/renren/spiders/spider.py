# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'

    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'

        data = {
            'email': '15112286305',
            'password': 'cuco2018',
        }  # 构造表单数据
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        url2 = 'http://www.renren.com/880792860/profile'

        request = scrapy.Request(url2, callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('baobeier.html', 'w', encoding='utf-8') as f:  # 写入文件
            f.write(response.text)
            f.close()
