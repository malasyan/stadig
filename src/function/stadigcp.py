#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ************
# 脚本接受的参数
# ************

import sys, getopt

def main(argv):
    date = ''
    time = ''
    minute = ''

    try:
        opts, args = getopt.getopt(argv, "hd:t:m:", ["indate=", "intime=", "inminute="])
    except getopt.GetoptError:
        print('stadigcp.py -d <yyyy-mm-dd> -t <xxxx> -m <int>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('stadigcp.py -d <yyyy-mm-dd> -t <xxxx> -m <int>')
            sys.exit()
        elif opt in ("-d", "--indate"):
            date = arg
        elif opt in ("-t", "--intime"):
            time = arg
        elif opt in ("-m", "--inminute"):
            minute = arg

    print('测试日期为：', date)
    print('起始时间为：', time)
    print('持续时间为:', minute)

if __name__ == "__main__":
   main(sys.argv[1:])

