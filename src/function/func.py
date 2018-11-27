#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# *******
# 公共函数
# *******

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

# 定义一个函数:将一行统计日志,转换成字典
# x 字符串
def string_dic(x):
    record = x[x.find('#') + 1 : x.rfind('#')]
    content = x[x.rfind('#') + 1:x.rfind('\n')].split('$')
    list = [['item', record]]
    for c in content:
        y = c.split('=')
        list.append(y)
    dic = dict(list)
    return dic


# 定义一个函数:将日志分析并输出成报告,内容是统计日志执行了哪些操作,记录了哪些内容.
# mfile 已格式好的日志文件
# lfile 输出的报告文件
# mapst 统计字段的map
def report(mfile, lfile, mapst):
    with open(mfile, 'r', encoding='utf-8') as f:
        I = f.readlines()

    with open(lfile, 'a', encoding='utf-8') as fa:

        for i in I:
            if '#' in i:
                t = i[:i.find('#')]

                if i[i.find('#') + 1 : i.rfind('#')] == 'adinfo':
                    fa.write(t + ': 广告曝光\n')
                elif i[i.find('#') + 1 : i.rfind('#')] == 'pageinfo':
                    fa.write(t + ': pagen曝光\n')
                else:
                    dict_i = string_dic(i)
                    item = dict_i['item']

                    if item == 'action':
                        type = mapst[item]['type'][dict_i['type']]
                        fa.write(t + ': 执行了(%s)操作.\n' % type)
                    elif item == 'page':
                        type = mapst[item]['type'][dict_i['type']]
                        fa.write(t + ': 进入了(%s)(%s)页面.\n' % (type, dict_i['id']))
                    elif item == 'duration':
                        type = mapst[item]['type'][dict_i['type']]
                        fa.write(t + ': 在(%s)停留(%s)秒.\n' % (type, dict_i['sec']))
                    elif item == 'v':
                        yn = mapst[item]['yn'][dict_i['yn']]
                        fa.write(t + ': 在(%s),播放视频(%s)秒,(%s).\n' % (dict_i['ref'], dict_i['pdur'], yn))
                    elif item == 'adclick':
                        fa.write(t + ': 点击广告.\n')
                    elif item == 'in':
                        type = mapst[item]['type'][dict_i['type']]
                        status = mapst[item]['status'][dict_i['status']]
                        fa.write(t + ': (%s)客户端,用户状态:(%s).\n' % (type, status))
                    elif item == 'pushaccess':
                        pushtype = mapst[item]['pushtype'][dict_i['pushtype']]
                        fa.write(t + ': 收到推送,推送类型:(%s),推送通道:(%s).\n' % (pushtype, dict_i['ref']))
                    elif item == 'openpush':
                        type = mapst[item]['type'][dict_i['type']]
                        pushtype = mapst[item]['pushtype'][dict_i['pushtype']]
                        fa.write(t + ': (%s)打开推送,推送类型:(%s),推送通道:(%s).\n' % (type, pushtype, dict_i['ref']))
                    elif item == 'ts':
                        type = mapst[item]['type'][dict_i['type']]
                        fa.write(t + ': 在(%s)频道,(%s)页面,进行了分享操作.\n' % (dict_i['ch'], type))
                    elif item == 'end':
                        if 'status' in dict_i:
                            status = mapst[item]['status'][dict_i['status']]
                            fa.write(t + ': (%s)客户端,此次客户端运行时长(%s)秒.\n' % (status, dict_i['odur']))
                        else:
                            fa.write(t + ': 退出客户端,此次客户端运行时长(%s)秒.\n' % dict_i['odur'])
                    elif item == 'desktop':
                        op = mapst[item]['op'][dict_i['op']]
                        fa.write(t + '(%s).\n' % op)
                    elif item == 'login':
                        type = mapst[item]['type'][dict_i['type']]
                        fa.write(t + ': 用户用(%s)登录客户端.\n' % type)
                    elif item == 'except':
                        fa.write(t + ': 客户端异常退出.\n')
                    elif item == 'hb':
                        fa.write(t + ': 心跳tm=%s\n' % dict_i['tm'])
                    elif item == 'shumeng':
                        fa.write(t + ': 数盟统计\n')
                    else:
                        fa.write(i)
            else:
                fa.write(i)
























