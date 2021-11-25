# _*_ coding:utf-8 _*_

"""
时间:2021年10月23日
作者:幻非
"""

import cv2
import os
import random
import string


def get_water(self):
    """去除logo的主程序"""
    # 读取图片
    src = cv2.imread(self)
    # 读取水印图片
    path = black_logo(self)
    mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 去除水印
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_NS)
    # 保存图片
    # cv2.imwrite('new\\' + str(getKey(10)) + ".jpeg", dst)  # 随机名称
    cv2.imwrite('new\\' + os.path.basename(self), dst)  # 原始名称
    os.remove(path)


def black_logo(self):
    """为了去除LOGO,将图片以外的部位涂黑,返回涂黑的图片地址"""
    # 读取图片
    image = cv2.imread(self)
    # 获取图片尺寸
    shape = image.shape
    # 截取logo图片
    corner = image[int(shape[0]*0.92):shape[0], int(shape[1]*0.85):shape[1]]
    # 保存读取作为变量
    cv2.imwrite('_.jpeg', corner)
    bg = cv2.imread('_.jpeg')
    os.remove('_.jpeg')
    # 图片全部涂黑
    image[0:shape[0], 0:shape[1]] = (0, 0, 0)
    # 将读取的logo图片放到原本的位置
    image[int(shape[0]*0.92):shape[0], int(shape[1]*0.85):shape[1]] = bg
    # cv2.imshow('original image', image)
    # 保存图片
    path = str(getKey(10)) + ".jpeg"
    cv2.imwrite(path, image)
    # cv2.waitKey(0)
    return path


def getKey(self):
    """返回指定数量的随机码"""
    data = string.ascii_letters + string.digits
    key = random.sample(data, self)
    keys = "".join(key)
    return keys


if __name__ == "__main__":
    black_logo('old\\1634916832704.jpeg')
