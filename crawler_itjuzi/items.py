# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()
    levelOneZone = scrapy.Field()
    levelTwoZone = scrapy.Field()
    tag = scrapy.Field()
    website = scrapy.Field()

    levelOneClass = scrapy.Field()
    levelTwoClass = scrapy.Field()
    fullName = scrapy.Field()
    setUpTime = scrapy.Field()
    available = scrapy.Field()

