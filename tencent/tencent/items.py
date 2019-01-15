# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 岗位名称
    positionname = scrapy.Field()
    # 岗位连接
    positionLike = scrapy.Field()
    # 岗位类型
    positionType = scrapy.Field()
    # 招聘人数
    peopleNum = scrapy.Field()
    # 工作地点
    workloaction = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
