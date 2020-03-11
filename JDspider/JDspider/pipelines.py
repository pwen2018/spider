# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdspiderPipeline(object):
    def __init__(self):
    #建立连接
        self.conn = pymysql.connect('localhost','root','123456','scrapy_db',charset='utf8')
    #创建游标
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        # sql语句
        insert_sql = '''
        insert into jd_shop_spider(p_commit,p_img,p_name,p_price,p_shop,p_shop_name,p_type) values (%s,%s,%s,%s,%s,%s,%s)
        '''
        # 执行sel语句
        self.cursor.execute(insert_sql,(item['p_commit'],item['p_img'],item['p_name'],item['p_price'],item['p_shop'],item['p_shop_name'],item['p_type']))
        # 提交
        self.conn.commit()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()