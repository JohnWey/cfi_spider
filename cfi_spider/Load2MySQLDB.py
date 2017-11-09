#-*- coding: utf-8 -*-
import ConfigParser
from MySqlTool import *
import time

reload(sys)
sys.setdefaultencoding('utf-8')

day = time.strftime('%Y%m%d',time.localtime(time.time()))
conf = ConfigParser.ConfigParser()
conf.read('mysql.conf')
conn = init_db(conf, 'Database')


def load2Mysql(type):
    hdngs = ''
    tabname = ''
    filename = ''


    if type == 'cwfxzb':
        hdngs = conf.get('Database', 'hdngs_cwfxzb')
        tabname = conf.get('Database', 'tabname_cwfxzb')
        filename = conf.get('Database', 'path_readFromFile').replace('?filename', 'cfi_cwfxzb_2012_2017')



    #数据日期
    #reportDT_list = ['2016']
    #print filename+reportDT_list[0]
    #f = open(filename + reportDT_list[0] + '.txt', 'r', 1)
    f = open(filename + '.txt', 'r', 1)

    for line in f:
        # print line
        cnt = len(line.split(','))

        if cnt == 171 :
            insert_demo(conn, tabname, hdngs, line)

        elif line.find('NONE')>=0:
            continue
        else:
            print "==================Exception=================="
            print cnt
            print line
            break
    close_conn(conn)

if __name__ == '__main__':
    #load2Mysql('balancesheet')
    #load2Mysql('cashflow')
    #load2Mysql('profit')
     load2Mysql('cwfxzb')

