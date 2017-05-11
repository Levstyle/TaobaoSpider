# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TbItem(scrapy.Item):
    # define the fields for your item here like:
    trade, comments = scrapy.Field(), scrapy.Field()
    item_id,item_name = scrapy.Field(),scrapy.Field()
