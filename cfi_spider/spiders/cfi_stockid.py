#-*- coding: utf-8 -*-
#Autor Zhang Wei

import os, sys
import time
import ConfigParser
from scrapy.spiders import Spider
from scrapy.selector import Selector


day = time.strftime('%Y%m%d',time.localtime(time.time()))


#读取配置文件获取股票代码等信息
conf = ConfigParser.ConfigParser()
conf.read('Stock.conf')
stockcodes = conf.get('Stock', 'stockcodes')
path_outputfile = conf.get('Stock', 'path_outputfile').replace('?filename','stockid')
urls = conf.get('Stock','url_link')

stockcode_list = [ x.replace("\'","") for x in stockcodes.split(',') ]


sys.stdout=open(path_outputfile+'.txt','w')



class CFI_StockIDCrawl(Spider):
    name = "cfi_stockid"
    allowed_domains = []

    start_urls = [urls.replace('?stockcode', str(stockcode_list[ii]))
                  for ii in range(0, len(stockcode_list))]


    def parse(self, response):
        #reload(sys)
        #sys.setdefaultencoding('utf-8')

        sel = Selector(response)
        v_link = sel.xpath('//*[@id="nodea1"]/nobr/a/@href').extract()[0]  #Result: /cwfxzb/11411/300146.html
        v_mapper = v_link.split("/")
        print v_mapper[2]
        #print v_mapper[2]+'/'+v_mapper[3]


        #插入数据到Mysql

        #运行 scrapy runspider cfi_spider.py




