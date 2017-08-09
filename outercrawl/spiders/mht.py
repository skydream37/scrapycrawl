# -*- coding: utf-8 -*-
import scrapy
import re
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs4
from outercrawl.items import OutercrawlItem


# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

class MhtSpider(scrapy.Spider):
    name = 'mht'
    # allowed_domains = ['https://tw.mall.yahoo.com/']
    start_urls = [
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=0',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=48',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=96',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=144',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=192',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=240',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=288',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=336',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=384',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=432',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=480',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=528',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=576',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=624',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=672',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=720',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=768',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=816',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=864',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=912',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=960',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1008',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1056',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1104',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1152',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1200',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1248',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1296',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1344',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1392',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1440',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1488',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1536',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1584',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1632',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1680',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1728',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1776',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1824',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1872',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1920',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=1968',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=2016',
        'https://tw.mall.yahoo.com/search?m=list&sid=mht&s=-salerank&view=both&b=2064'
    ]

    def parse(self, response):
        domain = 'https://tw.mall.yahoo.com/'
        soup = bs4(response.body)
        for pro_link in soup.select('.title a'):
            print(pro_link['href'])
            yield scrapy.Request(pro_link['href'], self.parse_detail)

    def parse_detail(self, response):
        pro_soup = bs4(response.body)
        # print(pro_soup.select_one('div > h1 > span').text)
        outercrawlitem = OutercrawlItem()
        outercrawlitem['store'] = '美華泰'
        outercrawlitem['current_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        outercrawlitem['name'] = pro_soup.select_one('div > h1 > span').text
        outercrawlitem['price'] = pro_soup.select_one('div > span.price').text
        outercrawlitem['link'] = response
        outercrawlitem['fee'] = 50
        try:
            outercrawlitem['sell'] = pro_soup.select('div.left > ul > li')[3].text
        except:
            outercrawlitem['sell'] = pro_soup.select('div.left > ul > li')[2].text
        # print(s1item['price'])
        # pro_soup.select('.slectit , h1 span').text
        return outercrawlitem
