#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ******************
# 统计日志自动化比对脚本
# ******************

import sys, urllib, os
from urllib import parse

from function import stadigcp
from function import func

# 调用命令行输入参数函数
stadigcp.main(sys.argv[1:])

# 获得基本参数
date = sys.argv[2]
time = sys.argv[4]
minute = int(sys.argv[6])

domain = 'http://10.80.130.149/newsapp_src/'
finduserkey = 'userkey=355907743cb240b0b9ed8bae53e44da9'


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

    with open('./outputs/log.txt', "a", encoding="utf-8") as f_log:
        for i in I:
            if finduserkey in i:
                # 执行两次urldecode
                i_urldecode = urllib.parse.unquote(i, encoding="utf-8", errors="replace")
                i_urlredecode = urllib.parse.unquote(i_urldecode, encoding="utf-8", errors="replace")

                # 获得session的起始位置
                if i_urlredecode.find('iPhone;') == -1:
                    session_begin = i_urlredecode.find('session=')
                    session_end = i_urlredecode.find('HTTP/1.1"')
                else:
                    session_begin = i_urlredecode.find('session=')
                    session_end = i_urlredecode.find('datatype=')

                # 截取session
                logse = i_urlredecode[session_begin + 8:session_end - 1]


                if i_urlredecode.find('datatype=newsapp') == -1:
                    print("datatype error in line %s" % (n+1))
                else:
                    f_log.write(logse + '\n')


                # 多此一举,暂时无用
                # # 获得datatype的起始位置
                # if i_urlredecode.find('iPhone;') == -1:
                #     dt_begin = i_urlredecode.find('datatype=')
                #     dt_end = i_urlredecode.find('&')
                # else:
                #     dt_begin = i_urlredecode.find('datatype=')
                #     dt_end = i_urlredecode.find('&idfa=')
                #
                # # 截取datatype
                # logdt = i_urlredecode[dt_begin:dt_end]

                # if dt_begin == -1:
                #     log = 'datatype=null&' + logse
                # else:
                #     log = logdt + '&' + logse
                #
                # f_log.write(log + '\n')

    #os.remove("./temp/" + stafile)
    n = n + 1
    time = func.tsum(date, time, 1)

# 按@符号分隔统计
func.string_switch("./outputs/log.txt", "@", "\n", "g")

# 过滤无用统计
with open("./outputs/log.txt", "r", encoding="utf-8") as r_log:
    I = r_log.readlines()

with open("./outputs/statistics_" + date + ".txt", "a", encoding="utf-8") as w_logc:
    for i in I:
        if '#hb#' in i or '#shumeng#' in i or '#pushaccess#' in i:
            continue
        else:
            w_logc.write(i)

if os.path.exists("./outputs/log.txt"):
    os.remove("./outputs/log.txt")

print("log complete!")
print("split log...")

#func.compare("./mould/mould.txt", "./outputs/log.txt", "/outputs/report.html")











