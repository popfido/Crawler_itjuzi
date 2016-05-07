# -*- coding: utf-8 -*-
import scrapy
from crawler_itjuzi.items import CompanyItem
import crawler_itjuzi.replica

# 34641

class companySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["itjuzi.com"]
    start_urls = ["http://www.itjuzi.com/company?page=%s" % page for page in range(1, 2493)] + \
                 ["http://www.itjuzi.com/company/foreign?page=%s" % page for page in range(1, 401)]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="list-main-icnset"]/li'):
            name = sel.xpath('p/a/span/text()').extract()[0]
            url = sel.xpath('p/a/@href').extract()[0]
            if url not in crawler_itjuzi.replica.rep:
                yield scrapy.Request(url, callback=self.parseCompany, meta={'name': name, 'url': url})

    def parseCompany(self, response):
        item = CompanyItem()
        info = response.xpath('//div[@class="info-line"]//a/text()').extract()
        des_info = response.xpath('//div[@class="des-more"]/div/span/text()').extract()

        if len(response.xpath('//div[contains(@class, "rowhead")]//img/@src').extract()) > 0:
            item['avatar'] = response.xpath('//div[contains(@class, "rowhead")]//img/@src').extract()[0]
        else:
            item['avatar'] = ''
        item['name'] = response.meta['name']
        item['url'] = response.meta['url']
        item['levelOneClass'] = info[0]
        item['levelTwoClass'] = info[1]
        item['levelOneZone'] = info[2]
        if len(info) > 3:
            item['levelTwoZone'] = info[3]
        else:
            item['levelTwoZone'] = ''
        item['website'] = response.xpath('//div[@class="link-line"]//a/@href').extract()[0]
        item['tag'] = ','.join(response.xpath('//div[@class="rowfoot"]//a/span/text()').extract())
        item['fullName'] = des_info[0][5:]
        item['setUpTime'] = des_info[1][5:]
        item['available'] = des_info[2]
        yield item