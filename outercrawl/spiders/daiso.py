# -*- coding: utf-8 -*-
import scrapy
import re
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs4
from outercrawl.items import OutercrawlItem


# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

class DaisoSpider(scrapy.Spider):
    name = 'daiso'
    # allowed_domains = ['https://tw.mall.yahoo.com/']
    start_urls = [
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=0',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=48',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=96',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=144',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=192',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=240',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=288',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=336',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=384',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=432',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=480',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=528',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=576',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=624',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=672',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=720',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=768',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=816',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=864',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=912',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=960',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1008',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1056',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1104',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1152',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1200',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1248',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1296',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1344',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1392',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1440',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1488',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1536',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1584',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1632',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1680',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1728',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1776',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1824',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1872',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1920',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=1968',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2016',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2064',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2112',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2160',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2208',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2256',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2304',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2352',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2400',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2448',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2496',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2544',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2592',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2640',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2688',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2736',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2784',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2832',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2880',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2928',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=2976',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3024',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3072',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3120',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3168',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3216',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3264',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3312',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3360',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3408',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3456',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3504',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3552',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3600',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3648',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3696',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3744',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3792',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3840',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3888',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3936',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=3984',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4032',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4080',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4128',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4176',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4224',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4272',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4320',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4368',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4416',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4464',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4512',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4560',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4608',
        'https://tw.mall.yahoo.com/search?m=list&sid=daiso&s=-sc_salerank&view=both&b=4656'
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=('&view=both&b=', )), callback='parse_list'),
    # )

    def parse(self, response):
        domain = 'https://tw.mall.yahoo.com/'
        soup = bs4(response.body)
        for pro_link in soup.select('#ypsausit .title a'):
            # print(pro_link['href'])
            yield scrapy.Request(pro_link['href'], self.parse_detail)

    def parse_detail(self, response):
        pro_soup = bs4(response.body)
        # print(pro_soup.select_one('div > h1 > span').text)
        outercrawlitem = OutercrawlItem()
        outercrawlitem['store'] = '大創'
        outercrawlitem['current_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        outercrawlitem['name'] = pro_soup.select_one('div > h1 > span').text
        outercrawlitem['price'] = pro_soup.select_one('div > span.price').text
        outercrawlitem['link'] = response
        outercrawlitem['fee'] = 50
        outercrawlitem['sell'] = pro_soup.select('div.left > ul > li')[3].text
        # print(outercrawlitem['price'])
        # pro_soup.select('.slectit , h1 span').text
        return outercrawlitem
