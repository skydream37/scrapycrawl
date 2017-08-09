# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OutercrawlItem(scrapy.Item):  # 輸出內容
    # define the fields for your item here like:
    # name = scrapy.Field()
    store = scrapy.Field()
    current_time = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    fee = scrapy.Field()
    sell = scrapy.Field()

    print(name, price)
