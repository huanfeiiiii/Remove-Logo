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

undone = []
for file in os.listdir('.\\old'):
    if os.path.splitext(file)[1] == ".jpeg" or os.path.splitext(file)[1] == ".png" or os.path.splitext(file)[1] == ".webp":
        print(file)
        logo.get_water('old\\' + file)
    else:
        undone.append(file)
for i in undone:
    print(f"这些图片的类型不支持:{i}")
