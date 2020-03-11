# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品图片
    p_img = scrapy.Field()
    # 商品价格
    p_price = scrapy.Field()
    # 商品名称
    p_name = scrapy.Field()
    # 评论链接
    p_commit = scrapy.Field()
    # 商家链接
    p_shop = scrapy.Field()
    # 商家名称
    p_shop_name = scrapy.Field()
    # 类型
    p_type = scrapy.Field()
