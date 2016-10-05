#!/usr/bin/python
from scrapy import Spider, Item, Field
from pymongo import MongoClient
import re

class Stock(Item):
        _id = Field()
        name = Field()
        actual = Field()
        high = Field()
        low = Field()
        chg = Field()
        vol = Field()

class Spider(Spider):

        name, start_urls = 'Most_All_Stocks', ['http://www.investing.com/indices/nasdaq-composite-components']

        def parse(self, response):
                client = MongoClient("mongodb://crawler:3ny3H94A@ds035006.mlab.com:35006/hot_stocks")
                db = client.hot_stocks

                db.hot_active_stocks.delete_many({})
                stocks = db.hot_active_stocks

                for table in response.css('table.crossRatesTbl'):
                        for tr in table.css('tbody > tr'):
                                chgStr = str(tr.xpath('td[7]/text()').extract())
                                chgReplaced = chgStr.replace('%','').replace("[u'","").replace("']","")
                                stock = Stock(name=tr.css('td > a::text').extract(), actual=tr.xpath('td[3]/text()').extract(), high=tr.xpath('td[4]/text()').extract(),
                                                                low=tr.xpath('tr[5]/text()').extract(), chg=chgReplaced,
                                                                vol=tr.xpath('td[7]/text()').extract())

                                stock_id = stocks.insert_one(stock).inserted_id
