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
stockid = conf.get('Stock', 'stockid')
path_outputfile = conf.get('Stock', 'path_outputfile').replace('?filename','cfi_cwfxzb_2012_2017')
urls = conf.get('Stock','cwfxzb_url_link')

stockid_list = [ x.replace("\'","") for x in stockid.split(',') ]

#stockid_list = ['1039']
reportDT_list = ['2017','2016','2015','2014','2013','2012']
sys.stdout=open(path_outputfile+'.txt','w')



class CFI_CWFXZB(Spider):
    name = "cfi_cwfxzb"
    allowed_domains = []

    start_urls = [urls.replace('?stockid', str(stockid_list[ii])).replace('?fiscal_yr',str(reportDT_list[jj]))
                  for ii in range(0, len(stockid_list)) for jj in range(0,len(reportDT_list)) ]


    def parse(self, response):
        #reload(sys)
        #sys.setdefaultencoding('utf-8')

        sel = Selector(response)
        v_stockcode = sel.xpath('//*[@id="nodea0"]/nobr/a/@href').extract()[0]
        v_stockcode_std = v_stockcode.split('/')[1].split('.')[0]
        v_cnt = sel.xpath('count(//td[@id="content"]/div[2]/table/tr[2]/td)').extract()[0]
        i = int(v_cnt[0])
        #print i
        #插入数据到Mysql
        for v_col_index in range(2, i + 1):
            v_url = "//table[@class='vertical_table']//tr//td[" + str(v_col_index) + "]/font/text()"
            v_itemSet = sel.xpath(v_url).extract()
            #print v_itemSet
            v_itemSet_fmt = [x.replace(',', '').replace(u'(元)','') for x in v_itemSet]
            print "\'" + v_stockcode_std + "\'"  + ',\''+ v_itemSet_fmt[0] + '\','+','.join(v_itemSet_fmt[1:-2]).replace("--","0")


        #运行 scrapy runspider cfi_spider.py




