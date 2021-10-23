# _*_ coding:utf-8 _*_

"""
时间:2021年10月23日
作者:幻非
"""

import cv2
import os

import get_logo


def get_water(self):
    # 读取图片
    src = cv2.imread(self)
    # 读取水印图片
    path = get_logo.black_logo(self)
    mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 去除水印
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_NS)
    # 保存图片
    cv2.imwrite(str(get_logo.getKey(10)) + ".jpeg", dst)  # 随机名称
    # cv2.imwrite(self, dst)  # 直接覆盖
    os.remove(path)


if __name__ == "__main__":
    get_water('1601821608664.jpeg')

