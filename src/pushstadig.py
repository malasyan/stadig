#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib,os
from urllib import parse
from datetime import datetime,timedelta

from function import func


# 获得日期
now = datetime.now()
yesterday = now - timedelta(days=1)
date = yesterday.strftime('%Y-%m-%d')
time = '0800'
minute = 10

domain = 'http://10.80.130.149/newsapp_src/'
finduserkey = ['352049073522022',
               '866932035508313',
               '9109cf4d98a40067',
               'b16ed6152eaf0f5ed0a0f9e092f24adda6922d9f',
               '358374067863099',
               '866479022917412']

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
    func.download(url, filename, stafile)

    # 筛选有用日志
    with open(stafile, "r", encoding="utf-8") as f_sta:
        I = f_sta.readlines()

    with open('./outputs/pushlog_%s.txt' % date , "a", encoding="utf-8") as f_log:
        for i in I:
            for a in finduserkey:
                if a in i:
                    # 执行两次urldecode
                    i_urldecode = urllib.parse.unquote(i, encoding="utf-8", errors="replace")
                    i_urlredecode = urllib.parse.unquote(i_urldecode, encoding="utf-8", errors="replace")

                    if '#pushaccess#' in i_urlredecode:
                        f_log.write(i_urlredecode + '\n')
                    else:
                        continue

    os.remove(stafile)

    n = n + 1
    time = func.tsum(date, time, 1)

print("down!")
