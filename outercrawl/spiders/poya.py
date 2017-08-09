# -*- coding: utf-8 -*-
import scrapy
import re
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs4
from outercrawl.items import OutercrawlItem


# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


class PoyaSpider(scrapy.Spider):
    name = 'poya'
    # allowed_domains = ['https://tw.mall.yahoo.com/']
    start_urls = [
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=0',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=48',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=96',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=144',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=192',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=240',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=288',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=336',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=384',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=432',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=480',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=528',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=576',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=624',
        'https://tw.mall.yahoo.com/search?m=list&sid=poya&s=-sc_salerank&view=both&b=672'
    ]

    # rules = [  #rule正規抓取出錯
    #     Rule(LinkExtractor(allow=('&view=both&b=[0-9][0-9]$')), callback='parse_list', follow=True)
    # ]

    def parse(self, response):
        domain = 'https://tw.mall.yahoo.com/'
        soup = bs4(response.body)
        for pro_link in soup.select('.title a'):  # 取得商品連結 送到requests
            # print(pro_link['href'])
            yield scrapy.Request(pro_link['href'], self.parse_detail)

    def parse_detail(self, response):
        pro_soup = bs4(response.body)
        # print(pro_soup.select_one('div > h1 > span').text)
        outercrawlitem = OutercrawlItem()
        outercrawlitem['store'] = '寶雅'
        outercrawlitem['current_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        outercrawlitem['name'] = pro_soup.select_one('div > h1 > span').text
        outercrawlitem['price'] = pro_soup.select_one('div > span.price').text
        outercrawlitem['link'] = response
        outercrawlitem['fee'] = 50
        outercrawlitem['sell'] = pro_soup.select('div.left > ul > li')[2].text
        # print(s1item['price'])
        # pro_soup.select('.slectit , h1 span').text
        return outercrawlitem
