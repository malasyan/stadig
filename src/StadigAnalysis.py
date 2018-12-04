#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# **********
# 统计日志分析
# **********


import urllib,os
from urllib import parse
from datetime import datetime,timedelta

from function import func
from data import statis_item


# 获得日期
now = datetime.now()
yesterday = now - timedelta(days=1)
date = yesterday.strftime('%Y-%m-%d')
time = '0900'
minute = 720

domain = 'http://10.80.130.149/newsapp_src/'
finduserkey = statis_item.finduserkey
mapst = statis_item.mapst

print('begin download...')

n = 0
m = minute
while n < m:

    # 获得下载链接,压缩文件名,解压后的文件名
    url = domain + date + '/' + time + '.sta.gz'
    filename = time + '.sta.gz'
    stafile = time + '.sta'
    print(url)

    # 执行下载&解压
    func.download(url, "./temp/" + filename, "./temp/" + stafile)

    # 筛选有用日志
    with open("./temp/" + stafile, "r", encoding="utf-8") as f_sta:
        I = f_sta.readlines()

    with open('./outputs/alog_%s.txt' % date, "a", encoding="utf-8") as f_log:
        for i in I:
            for a in finduserkey:
                if a in i:
                    # 执行两次urldecode
                    i_urldecode = urllib.parse.unquote(i, encoding="utf-8", errors="replace")
                    i_urlredecode = urllib.parse.unquote(i_urldecode, encoding="utf-8", errors="replace")

                    if i_urlredecode.find('datatype=newsapp') == -1:
                        f_log.write('userkey=' + a + '*' + i_urlredecode + '\n')
                    else:
                        # 获得session的起止位置
                        if i_urlredecode.find('iPhone;') == -1:
                            session_begin = i_urlredecode.find('session=')
                            middle = i_urlredecode[session_begin + 8:]
                            session_end = middle.find("&")
                            f_log.write('userkey=' + a + '*' + middle[:session_end] + '\n')
                        else:
                            session_begin = i_urlredecode.find('session=')
                            session_end = i_urlredecode.find('datatype=')
                            f_log.write('userkey=' + a + '*' + i_urlredecode[session_begin + 8:session_end - 1] + '\n')
                else:
                    continue

    os.remove("./temp/" + stafile)

    n = n + 1
    time = func.tsum(date, time, 1)

# 按userkey排序
with open('./outputs/alog_%s.txt' % date, "r", encoding="utf-8") as f_a:
    I = f_a.readlines()
with open('./outputs/analysislog_%s.txt' % date, "a", encoding="utf-8") as f_ana:
    for a in finduserkey:
        f_ana.write('userkey:%s\n' % a)
        for i in I:
            if a in i:
                f_ana.write(i[i.find('*') + 1:])
        f_ana.write('\n')

# 按@符号分隔统计
func.string_switch('./outputs/analysislog_%s.txt' % date, "@", "\n", "g")

# 生成报告
func.report('./outputs/analysislog_%s.txt' % date, './outputs/Analysis_log_%s.txt' % date, mapst)


