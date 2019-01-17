# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


class BaomaPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__),
                                 'images')  # os.path.dirname()获取当前文件的路径,os.path.join()获取当前目录并拼接成新目录
        if not os.path.exists(self.path):  # 判断路径是否存在
            os.mkdir(self.path)

    def process_item(self, item, spider):
        # 分类存储
        catagory = item['catagory']
        urls = item['urls']

        catagory_path = os.path.join(self.path, catagory)
        if not os.path.exists(catagory_path):  # 如果没有该路径即创建一个
            os.mkdir(catagory_path)

        for url in urls:
            image_name = url.split('_')[-1]  # 以_进行切割并取最后一个单元
            request.urlretrieve(url, os.path.join(catagory_path, image_name))

        return item
