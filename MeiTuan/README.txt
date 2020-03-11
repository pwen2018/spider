1.店铺接口:http://i.waimai.meituan.com/openh5/homepage/poilist
    1_1.headers:cookie,user_agent
    1_2.FormData:startIndex(翻页),wm_latitude(地理位置的纬度),wm_longitude（地理位置的经度)
2.店铺中商品接口:http://i.waimai.meituan.com/openh5/poi/food
    2_1.headers:cookie,user_agent,referer
    2_2.FormData:mtWmPoiId(店铺ID),originUrl(来源),wm_latitude(地理位置的纬度),wm_longitude（地理位置的经度)
3.字体反爬:1.eot,woff,动态切换字体反爬的健值对。
4.封IP:被检测出异常需要使用高匿代理。

目录结构:
run.py:开始
setting.py:包含1.字体库 2.headers 3.FormData 4.保存路径与字体路径
shops.py:使用字体库进行处理数据
file/map.txt:上海市所有地区的坐标位置
file/AllOverTheCountry.txt:全国所有地区的坐标位置
file/meituanShopsItems.csv:采集到的数据