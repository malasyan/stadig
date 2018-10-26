#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import difflib
import gzip, shutil, urllib3
from datetime import datetime,timedelta


# 定义一个函数:下载&解压&删除压缩文件
# url 表示下载地址
# filename 表示压缩文件名(得包括格式后缀)
# stafile 表示解压后的文件名(得包括格式后缀)
def download(url, filename, stafile):

    http = urllib3.PoolManager()
    r = http.request("GET", url )

    with open(filename, "wb") as code:
        code.write(r.data)

    with gzip.open(filename, "rb") as read, open(stafile, "wb") as write:
        shutil.copyfileobj(read, write)

    if os.path.exists(filename):
        os.remove(filename)
    else:
        print('no such file:%s' %filename)


# 定义一个函数:计算增加N分钟数后的时间
# date 表示日期,格式为字符串yyyy-mm-dd
# time 表示小时和分钟,格式为字符串xxxx
# minute 表示所要加的分钟数,格式为整型
def tsum(date,time,minute):
    timebe = date + ' ' + time[:2] + ':' +time[2:]
    timestart = datetime.strptime(timebe, '%Y-%m-%d %H:%M')
    timeend = timestart + timedelta(minutes=minute)
    timeaf = timeend.strftime('%H:%M')
    return timeaf[:2] + timeaf[3:]


# 定义一个函数:替换分离，带有4个参数
# x 表示要更新的文件名称
# y 表示要被替换的内容
# z 表示 替换后的内容
# s 默认参数为 1 表示只替换第一个匹配到的字符串
# 如果参数为 s = 'g' 则表示全文替换
def string_switch(x, y, z, s=1):
    with open(x, "r", encoding="utf-8") as f:
        # readlines以列表的形式将文件读出
        lines = f.readlines()

    with open(x, "w", encoding="utf-8") as f_w:
        # 定义一个数字，用来记录在读取文件时在列表中的位置
        n = 0
        # 默认选项，只替换第一次匹配到的行中的字符串
        if s == 1:
            for line in lines:
                if y in line:
                    line = line.replace(y, z)
                    f_w.write(line)
                    n += 1
                    break
                f_w.write(line)
                n += 1
            # 将剩余的文本内容继续输出
            for i in range(n, len(lines)):
                f_w.write(lines[i])
        # 全局匹配替换
        elif s == 'g':
            for line in lines:
                if y in line:
                    line = line.replace(y, z)
                f_w.write(line)



#文件逐行读取
def getLines(file_name):
    return open(file_name).readlines()

# 定义一个函数:文本逐行比对,带有3个参数
# mfile 表示母文件
# lfile 表示对比文件
# report 表示输出结果的文件名
def compare(mfile,lfile,report):
    try:
        file1 = mfile
        file2 = lfile
        report = report

    except Exception as e:
        print('Error:' + str(e))
        sys.exit()

    txt_line1 = getLines(file1)
    txt_line2 = getLines(file2)

    d = difflib.HtmlDiff(wrapcolumn=75)
    fid = open(report, 'w')
    fid.write(d.make_file(txt_line1, txt_line2, context=True, numlines=5, charset='utf-8'))
    fid.close()


































