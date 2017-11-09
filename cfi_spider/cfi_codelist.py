#-*- coding: utf-8 -*-
#Autor Zhang Wei
import tushare as ts

"""
df = ts.get_hs300s()
#选择保存
df.to_csv('C:/Users/admin/Downloads/Code/WorkSpace/Python/cfi_spider/output/codelist.csv',columns=['code'],header=False,index=None)

df = ts.get_zz500s()

df.to_csv('C:/Users/admin/Downloads/Code/WorkSpace/Python/cfi_spider/output/codelist.csv',columns=['code'],header=False,index=None,mode='a')
"""

df = ts.get_industry_classified()
df.to_csv('C:/Users/admin/Downloads/Code/WorkSpace/Python/cfi_spider/output/codelist.csv',columns=['code'],header=False,index=None)
