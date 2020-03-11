# -*- coding: utf-8 -*-
# @author='yuewei'
# @Time:2019/8/8  14:49
import re
from setting import NUMBER1


class Shops():
    def __init__(self):
        pass

    # 商家信息处理
    def translate_number1(self, arg):
        arg = re.sub("起送| |配送|分钟|月售|¥|高峰|km|人均|夜间", "", arg)
        numbers = ""
        # 评论中含有+
        if re.search("\+", arg):
            arg = arg[:-2]
            for i in arg.split(";"):
                numbers += NUMBER1[i]
            numbers += "+"
        # 含有小数点
        elif re.search("\.", arg):
            arg = arg[:-1]
            for i in arg.replace(".", "").split(";"):
                arg = arg.replace(i, NUMBER1[i])
            # 去除分号
            numbers = arg.replace(";", "")
        else:
            arg = arg[:-1]
            for i in arg.split(";"):
                if i != "":
                    numbers += NUMBER1[i]
        return numbers

    # 打折商品处理
    def discount(self, arg):
        li = re.findall("&(.*?);", arg)
        for i in li:
            index = "&" + i
            arg = arg.replace(index, NUMBER1[index])
        return arg

    # 处理商家店铺商品
    def translate_number2(self, arg):
        arg = arg[:-1]
        numbers = ""
        for i in arg.split(";"):
            numbers += NUMBER1[i]
        return numbers


if __name__ == '__main__':
    pass
