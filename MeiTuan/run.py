# -*- coding: utf-8 -*-
# @author='yuewei'
# @Time:2019/8/8  15:55
import requests
from json import loads
from shops import Shops
import codecs
from setting import *
import time

shop = Shops()


# 商家
def start(startIndex, url, wm_latitude, wm_longitude):
    # 请求
    data = data1(startIndex, wm_latitude, wm_longitude)
    html = requests.post(url, headers=HEADERS, data=data).text
    print(html)
    # 转换成json
    data = loads(html)
    shop_list = data['data']["shopList"]
    # 取数据
    for i in shop_list:
        # 店铺ID
        mtWmPoiId = i["mtWmPoiId"]
        # 店铺名称
        shopName = i["shopName"]
        # 评分
        wmPoiScore = i["wmPoiScore"] / 10
        # 月售
        monthSalesTip = i["monthSalesTip"]
        monthSalesTip = shop.translate_number1(monthSalesTip)
        # 起送
        minPriceTip = i["minPriceTip"]
        minPriceTip = shop.translate_number1(minPriceTip)
        # 配送
        shippingFeeTip = i["shippingFeeTip"]
        shippingFeeTip = shop.translate_number1(shippingFeeTip)
        # 人均消费
        averagePriceTip = i["averagePriceTip"]
        averagePriceTip = shop.translate_number1(averagePriceTip)
        # 地址
        address = i["address"]
        # 优惠信息
        try:
            discounts2 = i["discounts2"][0]["info"]
            discounts2 = shop.discount(discounts2)
        except Exception as e:
            discounts2 = "暂无优惠"
        # 售卖商品信息
        shopInfo = ItemsData(mtWmPoiId.replace(" ", ""), wm_latitude, wm_longitude)
        # 保存数据
        with codecs.open(FILE_STORE, 'a', encoding="utf-8") as f:
            # 信息排序:店铺名称，星级，销量，地址，起送，配送，人均消费，促销信息，售卖商品名称;单价;月销量。。。。
            message = shopName + "," + str(
                wmPoiScore) + "," + monthSalesTip + "," + address + "," + minPriceTip + "," + shippingFeeTip + "," + averagePriceTip + "," + discounts2 + "," + shopInfo + "," + "\n"
            print(message)
            f.write(message)

    return "ok"


# 商品信息
def ItemsData(mtWmPoiId, wm_latitude, wm_longitude):
    time.sleep(3)
    url2 = 'http://i.waimai.meituan.com/openh5/poi/food'
    dataItems = data2(mtWmPoiId, wm_latitude, wm_longitude)
    html2 = requests.post(url2, headers=headers2(mtWmPoiId), data=dataItems).text
    data = loads(html2)

    # 商品列表
    categoryList = data["data"]["categoryList"]
    # 将所有商品拼接成字符串
    items = ""
    for i in categoryList:
        # 标题名称的内容
        spuList = i["spuList"]
        for j in spuList:
            # 售卖商品名称
            spuName = j["spuName"]
            # 月售
            saleVolumeDecoded = shop.translate_number2(j["saleVolumeDecoded"])
            # 当前价格
            currentPrice = j["currentPrice"]
            # 商品总和
            items += spuName + ";" + saleVolumeDecoded + ";" + str(currentPrice) + '。'
    return items


if __name__ == '__main__':
    # 所有商家接口
    # url = 'http://i.waimai.meituan.com/openh5/homepage/poilist'
    url = 'http://i.waimai.meituan.com/openh5/channel/kingkongshoplist'
    with open(MAP_STORE, 'r') as f:
        location = f.read().split("\n")
        del location[-1]
        for i in location:
            wm_longitude = i.split(",")[0]
            wm_latitude = i.split(",")[1]
            # 当前经纬度
            print("wm_longitude：", wm_longitude, "wm_latitude", wm_latitude)
            for page in range(6):
                print("当前页面:", page)
                # 通过try ... catch 捕捉异常
                try:
                    start(page, url, wm_latitude, wm_longitude)
                except Exception as e:
                    time.sleep(10)
                    print(e)
