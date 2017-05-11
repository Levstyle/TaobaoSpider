# -*- coding: utf-8 -*-
import scrapy
from TB.items import TbItem
from scrapy import Request, Selector
from selenium import webdriver
from urllib.parse import urlparse,parse_qs

class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ['https://item.taobao.com/item.htm?spm=a230r.1.14.75.4BT18i&id=538224140282&ns=1&abbucket=8',
                  'https://item.taobao.com/item.htm?spm=a230r.1.14.259.fxI6M3&id=533150330578&ns=1&abbucket=8#detail',
                  'https://item.taobao.com/item.htm?spm=a230r.1.14.15.fjTlaf&id=549299824849&ns=1&abbucket=8#detail']

    # //*[@id="J_Title"]/h3
    def __init__(self, *args, **kwargs):
        super(TaobaoSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(30)
        selector = Selector(text=self.driver.page_source)
        for sel in selector.xpath('//*[@id="J_Counter"]'):
            item = TbItem()
            item['comments'] = sel.xpath('//*[@id="J_RateCounter"]/text()').extract_first()
            item['trade'] = sel.xpath('//*[@id="J_SellCounter"]/text()').extract_first()
            item['item_name'] = sel.xpath('//*[@id="J_Title"]/h3/@data-title').extract_first()
            item['item_id'] = parse_qs(urlparse(response.url).query, True)['id'][0]
            yield item

    def __del__(self):
        if self.driver is not None:
            self.driver.quit()
