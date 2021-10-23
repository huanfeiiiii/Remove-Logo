# _*_ coding:utf-8 _*_

"""
时间:2021年10月23日
作者:幻非
"""


import os

import logo


if not os.path.exists('old'):
    os.mkdir('old')
if not os.path.exists('new'):
    os.mkdir('new')


for file in os.listdir('.\\old'):
    print(file)
    logo.get_water('old\\' + file)
