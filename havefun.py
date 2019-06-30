#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:42:36 2019

@author: oliver_sun
"""

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import random
import time
import sys


g_counts = 1        # 游戏机会
g_classification = 0  # 题目类别
g_score = 0         # 当前分数
g_boolean = 2       # 答题正确为1，错误为0
g_help = 2          # 求助机会，共有2次

num_cas = 30        # 中科院类题目数量为30
num_literature = 52 # 文学、历史类题目数量为52
num_movie = 35      # 影视、娱乐类题目数量为35
num_sport = 31      # 运动、军事类题目数量为31
num_geography = 147 # 地理、百科类题目数量为147

path_cas = './cas/' 
path_literature = './literature/'
path_movie = './movie/'
path_sport = './sport/'
path_geography = './geography/'

list_cas = []
list_literature = []
list_movie = []
list_sport = []
list_geography = []

def get_help(l_help):
    flag = input("可以将问答题改为选择题哦：")
    print(" ")
    if flag == '1':
        l_help = l_help - 1
    return l_help
    

def end_game(l_boolean, l_score):
    '''
    如果答题失败结束游戏，显示对应奖品；否则继续游戏
    '''
    if l_boolean == '0':
        if l_score > 0:
            print("恭喜你获得参与奖！")
            print(" ")
            l_score = 0
        return l_boolean, l_score
    else:
        l_boolean = 2
        return l_boolean, l_score
        
def show_score(l_score):
    '''
    打印分数
    '''
    print('当前分数为：{0}'.format(l_score))
    print(" ")

def game(l_score, l_boolean, l_help, num, path, lists):
    '''
    题目回答程序
    '''
    # 随机选择题目
    number = random.randint(1, num)
    while number in lists:
        number = random.randint(1, num)
    lists.append(number)
    file_name = str(number)+'.png'
    open_path = path + file_name
    fig = mpimg.imread(open_path)
    fig.shape
    
    
    # 显示题目
    plt.imshow(fig)
    plt.axis('off')
    plt.ion()
    plt.show()
    
    
    # 寻求帮张
    if l_help > 0:
        l_help = get_help(l_help)
        

    # 确认答案
    l_boolean = input("若答对请输入1，否则输入0：")
    print(" ")
    while True:
        if l_boolean == '1':
            l_score = l_score + 1
            plt.close()
            print("恭喜恭喜，可以进入下一环节")
            print(" ")
            break;
        elif l_boolean == '0':
            plt.close()
            print("很遗憾答错了(´;︵;`)")
            print(" ")
            break;
        else:
            l_boolean = input("输入有误，请重新输入：")
            print(" ")
   
    return l_score, l_boolean, l_help, lists


print(" ")
print("欢迎参加草地音乐节游戏环节！祝你好运哦～")
print(" ")
print("如果你已经发了有关音乐节现场的朋友圈，请给我们看哦，可以获得一次复活机会！")
print(" ")
pengyouquan = input("请确认朋友圈内容(y/n)：")
print(" ")
 
   
# 确定朋友圈内容，判断是否拥有复活机会   
while True:
    if pengyouquan == 'y':
        g_counts = 2
        break;
    elif pengyouquan == 'n':
        g_counts = 1
        break;
    else:
        pengyouquan = input("输入有误，请重新输入：")
        print(" ")
    
for i in range(g_counts):
    if i == 1:
        time.sleep(1)
        print("把握好最后一次机会哦")
        print(" ")
    print("我们先从中科院知识点开始答题吧！")
    print(" ")
    show_score(g_score)
    time.sleep(1)
    [g_score, g_boolean, g_help, list_cas] = game(g_score, g_boolean, g_help, \
                                                num_cas, path_cas, list_cas)
    show_score(g_score)
    [g_boolean, g_score] = end_game(g_boolean, g_score)

    
    # 结束当前游戏
    if g_boolean == '0':
        g_boolean = 2
        if g_counts == 2:
            continue
        else:
            print("游戏结束，感谢参与，很遗憾没有奖品")
            print(" ")
            break
        
    
    done = input("请选择是否继续游戏，如果继续视为放弃已得奖品。确定继续请输入1：")
    print(" ")
    if done == '1':
        print("1：文学、历史类，2：影视、娱乐类，3：体育、军事类，4：地理、百科类")
        print(" ")
        g_classification = input("请从上述类别中选择1个：")
        print(" ")
    else:
        show_score(g_score)
        print("游戏结束，感谢参与，快去领奖吧")
        print(" ")
        break
         
    while (g_classification > '4'):
        g_classification = input("输入有误，请重新输入：")
        print(" ")
        
    if g_classification == '1':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_literature] = game(g_score, g_boolean, g_help, \
                                            num_literature, path_literature, list_literature)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '2':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_movie] = game(g_score, g_boolean, g_help, \
                                            num_movie, path_movie, list_movie)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '3':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_sport] = game(g_score, g_boolean, g_help, \
                                            num_sport, path_sport, list_sport)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '4':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_geography] = game(g_score, g_boolean, g_help, \
                                            num_geography, path_geography, list_geography)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    
    g_classification = 0;
    print("最后一个问题了，继续加油呀")
    print(" ")
    done = input("请选择是否继续游戏，如果继续视为放弃已得奖品。确定继续请输入1：")
    print(" ")
    if done == '1':
        print("1：文学、历史类，2：影视、娱乐类，3：体育、军事类，4：地理、百科类")
        print(" ")
        g_classification = input("请从上述类别中选择1个：")
        print(" ")
    else:
        show_score(g_score)
        print("游戏结束，感谢参与，快去领奖吧")
        print(" ")
        break
    while (g_classification > '4'):
        g_classification = input("输入有误，请重新输入：")
        print(" ")
        
    if g_classification == '1':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_literature] = game(g_score, g_boolean, g_help, \
                                            num_literature, path_literature, list_literature)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '2':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_movie] = game(g_score, g_boolean, g_help, \
                                            num_movie, path_movie, list_movie)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '3':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_sport] = game(g_score, g_boolean, g_help, \
                                            num_sport, path_sport, list_sport)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
    elif g_classification == '4':
        show_score(g_score)
        time.sleep(1)
        [g_score, g_boolean, g_help, list_geography] = game(g_score, g_boolean, g_help, \
                                            num_geography, path_geography, list_geography)
        show_score(g_score)
        [g_boolean, g_score] = end_game(g_boolean, g_score)
        if g_boolean == '0':
            g_boolean = 2
            if g_counts == 2:
                continue
            else:
                print("游戏结束，感谢参与，快去领奖吧")
                print(" ")
                break
            
    
    show_score(g_score)
    print("恭喜获得大奖，快去领奖吧！")
    print(" ")
    time.sleep(3)
    sys.exit(0)