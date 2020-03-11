# -*- coding: utf-8 -*-
import scrapy
from ..items import JdspiderItem
import re


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['search.jd.com/s_new.php']
    start_urls = ['http://https://search.jd.com/s_new.php']

    def start_requests(self):
        url = 'https://search.jd.com/s_new.php?keyword=%E8%A1%A3%E6%9C%8D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%A1%A3%E6%9C%8D&page=7&s=152&click=0'
        headers = {
            "referer": url.replace("s_new.php", "Search"),
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        item = JdspiderItem()
        contain = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for i in contain:
            # 商品图片
            item["p_img"] = "https:" + i.xpath('./div/div[@class="p-img"]/a/@href').extract_first().replace("https:",
                                                                                                            "")
            # 商品价格
            item["p_price"] = i.xpath('./div/div[@class="p-price"]//i/text()').extract_first()
            # 商品名称
            item["p_name"] = i.xpath('./div/div[@class="p-img"]/a/@title').extract_first()
            # 评论链接
            item["p_commit"] = "https:" + i.xpath('./div/div[@class="p-commit"]//a/@href').extract_first().replace(
                "https:", "")
            # 商家链接
            item["p_shop"] = i.xpath('./div/div[@class="p-shop"]//a/@href')
            # 商家名称
            item["p_shop_name"] = i.xpath('./div/div[@class="p-shop"]//a/@title')
            # 类型
            if len(item["p_shop"]) == 0 or len(item["p_shop_name"]) == 0:
                item["p_shop"] = ""
                item["p_shop_name"] = ""
                item["p_type"] = "广告"
            else:
                item["p_shop"] = "https:" + i.xpath('./div/div[@class="p-shop"]//a/@href').extract()[0].replace(
                    "https:", "")
                item["p_shop_name"] = i.xpath('./div/div[@class="p-shop"]//a/@title').extract()[0]
                item["p_type"] = "商品"
            yield item
        # 翻页
        url = response.request.url
        page_s = re.findall("page=(\d+)&s=(\d+)&", url)[0]
        page = int(page_s[0]) + 1
        s = int(page_s[1]) + 30
        next_url = re.sub("page=\d+&s=\d+&",'page={}&s={}&'.format(page,s),url)
        headers = {
            "referer": next_url.replace("s_new.php", "Search"),
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        yield scrapy.Request(next_url,headers=headers,callback=self.parse,dont_filter=True)