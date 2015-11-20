# -*- coding:utf-8 -*-

import sys
import random


IDIOM_FILE = '/home/haipeng/catkin_ws/src/qbo_chat_robot/scripts/chengyu_2col2.txt'
tbl_idiom = []  #每个成语有3列：编号，汉字序列，拼音序列
num_idiom = 0

inited = False

last_idiom = '' #最近一次发给用户的成语

def init_idioms():
    global inited,tbl_idiom, num_idiom
    f_idiom = open(IDIOM_FILE, 'r')

    for line in f_idiom:
        tbl_idiom.append(tuple(line.decode('utf-8').split(',')))  #读取文件注意unicode解码！
    f_idiom.close()
    inited = True

def send_idiom():
    global last_idiom
    index = random.randint(1, len(tbl_idiom))
    last_idiom = tbl_idiom[index][1]
    #print 'first idiom sent by qbo = %s' % last_idiom
    return last_idiom

def send_response(idiom):
    global tbl_idiom, last_idiom
    start_index, stop_index = 0, 0
    for record in tbl_idiom:
        word = record[1]
        if word.startswith(idiom[-1]) and 0 == start_index: #第一个首字匹配的索引
            start_index = int(record[0]) -1 #成语编号以1开始，而不是0
        if 0 != start_index and not word.startswith(idiom[-1]): #最后一个首字匹配的索引
            stop_index = int(record[0]) -1 -1 #成语编号以1开始，而不是0，第二个-1是因为当前record已不是首字匹配

            ret_index = random.randint(start_index, stop_index)
            last_idiom = tbl_idiom[ret_index][1] #随机返回一个首字匹配的
            return (True, last_idiom) #成功接龙！！！
    return (False, '我接不上，你赢了')

def start_jielong():
    if not inited:
        init_idioms()
    return send_idiom()

def jielong(word):
    global last_idiom
    if not word.startswith(last_idiom[-1]):
        return (False, u'%s不符合接龙规则，接龙结束'%word)
    for record in tbl_idiom:
        if record[1] == word:
            return send_response(word)
    return (False, u'我没听过%s这个成语，接龙结束'%word)
