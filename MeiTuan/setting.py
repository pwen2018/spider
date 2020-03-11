# -*- coding: utf-8 -*-
# @author='yuewei'
# @Time:2019/8/8  14:55

# 保存文件路径
FILE_STORE = './file/meituanShopsItems.csv'
MAP_STORE = './file/map.txt'

# 数字字体库
NUMBER1 = {
    "&#xf76a": "0",
    "&#xe81d": "1",
    "&#xe611": "2",
    "&#xe83e": "3",
    "&#xe8ff": "4",
    "&#xf881": "5",
    "&#xe7b9": "6",
    "&#xe180": "7",
    "&#xf36a": "8",
    "&#xe368": "9",

    "&#xe1de": "0",
    "&#xf75d": "1",
    "&#xe092": "2",
    "&#xe0a2": "3",
    "&#xf86f": "4",
    "&#xeef8": "5",
    "&#xe91c": "6",
    "&#xf89b": "7",
    "&#xf612": "8",
    "&#xe422": "9",

    "&#xf6d5": "0",
    "&#xf553": "1",
    "&#xeebc": "2",
    "&#xe10f": "3",
    "&#xe7e9": "4",
    "&#xf43f": "5",
    "&#xe23a": "6",
    "&#xe38a": "7",
    "&#xf741": "8",
    "&#xf509": "9",

    "&#xf568": "0",
    "&#xe956": "1",
    "&#xe2d0": "2",
    "&#xe372": "3",
    "&#xeb28": "4",
    "&#xe86c": "5",
    "&#xe3a0": "6",
    "&#xe130": "7",
    "&#xf848": "8",
    "&#xed42": "9",

    "&#xf0c1": "0",
    "&#xe066": "1",
    "&#xecf8": "2",
    "&#xe3ee": "3",
    "&#xef4b": "4",
    "&#xe279": "5",
    "&#xec1e": "6",
    "&#xebe9": "7",
    "&#xf6ea": "8",
    "&#xeedb": "9",
}

# 商家信息与参数
# 头信息
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Cookie': 'Cookie:_lxsdk_cuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; ci=50; _ga=GA1.3.9812869.1564225735; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=9758b710476f415cb70d.1564225729.1.0.0; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1565190856; __utma=211559370.241325758.1565190856.1565190856.1565190856.1; __utmz=211559370.1565190856.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; _lxsdk=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; _hc.v=da92c530-4541-68c8-c26b-e711c6edb63b.1565192909; __mta=142545421.1564225735797.1565196129183.1565196138000.5; wm_order_channel=default; utm_source=; openh5_uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; w_latlng=31375602,121265300; _lx_utm=utm_source%3D; cssVersion=876fcc61; au_trace_key_net=default; openh5_uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; w_visitid=2be6a38a-b55c-497c-b8aa-1c5196c0265b; _lxsdk_s=16c73b5fb01-f0b-b36-7a6%7C%7C5'
}


# 参数:页数，经度，纬度。
def data1(startIndex, wm_latitude, wm_longitude):
    DATA = {'startIndex': startIndex,
            'sortId': '0',
            'multiFilterIds': '',
            'sliderSelectCode': '',
            'sliderSelectMin': '',
            'sliderSelectMax': '',
            'geoType': '2',
            'rankTraceId': '',
            'uuid': '16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8',
            'platform': '3',
            'partner': '4',
            'originUrl': 'http://h5.waimai.meituan.com/waimai/mindex/home',
            'riskLevel': '71',
            'optimusCode': '10',
            'wm_latitude': wm_latitude,
            'wm_longitude': wm_longitude,
            'wm_actual_latitude': '',
            'wm_actual_longitude': '',
            'openh5_uuid': '16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8',
            '_token': 'eJxVj1uPokAQhf9Lv0KEbrBBk31g6V6HmyJ33cwDAiMXERUEx83+9+3Jug+bVHJOfXUqqfoFbkYOllCEigh5MBY3sARwJs4w4MHQs8kczyVxIUMFQoUH2X9MhRJjh1tEwPInlOaYR6r0/kU8BhjBmFew+s6/LGIWyay+MgaLgHIYLktBKOezKa3atJq1RTXc0/Ms61rhLxLa6pwXD6Hs2oIdBdhuG7Bdps1L05cO/3qHfcGyfXU8M1eYn6fGGTbTU9t6H9xJ5zifM6ls7c3Ep5W3o9E+QrJqWi6mQbOxE86N8TZGtpV1eFRaRzR2H9n8yNn0FhxKuuhoHxS20dKV+0yUPIzrljy074s7SSla2HH9dj/tUX8P0/S0Mba5mYbVcXfZP325wqsu65GeI+xqO1KdqG90SidhMwrF23MLo3WQnH1M/JjU+oAuOcnWoXQtH1jj8qt+VIzbyv2kP6L1/joGhVxudM+CLoert6smVY2X1b0waVEKa32KSeYlPdGbVDiO6tV2PyaCCTUdtKt8s4gn4WLltbDg5E2Air62FaJIz9IZkwRPspMpo95QisTaOgh6K3uPRxvW1hqqWp5aTU+/gd9/ABzJrmU='
            }
    return DATA


# ================================================================================
# 商品头信息与参数
# headers 中添加了refer cookie中添加w_visitid=11c6a687-0ae7-4ba0-bf88-ebd9166370a7;
def headers2(mtShopId):
    HEADERS = {
        'Cookie': '_lxsdk_cuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; ci=50; _ga=GA1.3.9812869.1564225735; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=9758b710476f415cb70d.1564225729.1.0.0; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1565190856; __utma=211559370.241325758.1565190856.1565190856.1565190856.1; __utmz=211559370.1565190856.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; _lxsdk=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; _hc.v=da92c530-4541-68c8-c26b-e711c6edb63b.1565192909; __mta=142545421.1564225735797.1565196129183.1565196138000.5; wm_order_channel=default; utm_source=; openh5_uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; w_latlng=31375602,121265300; _lx_utm=utm_source%3D; cssVersion=876fcc61; au_trace_key_net=default; openh5_uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; uuid=16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8; w_visitid=2be6a38a-b55c-497c-b8aa-1c5196c0265b; _lxsdk_s=16c73b5fb01-f0b-b36-7a6%7C%7C5',
        'Referer': 'http://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=%s' % mtShopId,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

    return HEADERS


# 参数:商品ID,精度,纬度。
def data2(mtShopId, wm_latitude, wm_longitude):
    DATA = {'geoType': '2', 'mtWmPoiId': mtShopId,
            'dpShopId': '-1', 'source': '', 'skuId': '',
            'uuid': '16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8',
            'platform': '3', 'partner': '4',
            'originUrl': 'http://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=%s' % mtShopId,
            'riskLevel': '71',
            'optimusCode': '10', 'wm_latitude': wm_latitude, 'wm_longitude': wm_longitude, 'wm_actual_latitude': '',
            'wm_actual_longitude': '', 'openh5_uuid': '16be8e9b37d49-0818768672ae4d-3c60460e-100200-16be8e9b37ec8',
            '_token': 'eJxNkdmOolAQht+FW4ichdWkLxBBpEVEFJdJX6CgKAI2CB6dzLvPgbHNJCTnS1X9fy38ZspxxPQhgDKAHNPEJdNnYA/0JIZjbhXNiJKIgSpAGUKZY/b/xSSAJUngmF0ZDJn+L4hFiUMK/mojcxqgEUniZEn54l6IKCKBfm3NmJYwye127fN8Ivbu4SkLT70sPt3qMO/ti4z/F+KzUx7FhE+KLKZDMVSbLVotVmUOIYXGIAYchrAlpL5JpgQ6kjgMujraHAOpI0xJ7AhSEt6EO6J+ALUEqR/o/Oj6GHR+kK6gdi4QUuoUQKXUKYBCqVMAOp8KfkhR36S8SX6T9OMid3UQc0gSX32RCF/zIUF6bYQE/NoXCV1fTBVCV4fbbNcX01mw2p4sbU9G37A7XXswRIcfjoM2eftJOvTvU111OuaUYvtxSR3o3p+al0zZy0BlfVaPiKX7E+0Rp9ZV0/ab535rZBXJdykaLGKriFfmbP35CJtteoh36LB+Kuw5I1DMBho+rksxSwf+VhmFcW5ID8NA01Ecg8l5dBvV86wazQLyncj+4TgYDD0raKJLiszB3AFmKWV6Vakbgi3bWXnGRriS6BwMbXWMvW0tzCbH2HascbyABcsWubvZ3DFZmyt3mV832K89IypKWxQBIZfj93nnsYfEM3by88AS67HdXc2z4+JTUataUdWy7cbpRdABXI7KMGT1rT7Po/2S4KUn+4ZtL/LcTN3CJxu+iQDZTfXqMLGSbZFffCGC4pjkj/ic14LnZKu5CyzX+YxwgxseRQurGYXTWRSY+rcS8plsacH0vj/TfmVtXnwyXCakvDUB1K9Y+/hg/vwFd5/7sw=='
            }
    return DATA
