# -*- coding: utf-8 -*-

""" 
@author: Jin.Fish
@file: util.py
@version: 1.0
@time: 2021/04/25 17:46:26
@contact: jinxy@pku.edu.cn

小工具
"""

def gen_param_md():
    while True:
        zh_name = input('请输入参数中文名：')
        en_name = input('请输入参数英文名')
        num = int(input('请输入栗子个数'))
        if not num:
            num = 1
        while num:

            num -= 1
