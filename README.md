# spider
网络爬虫
常用的软件包
查询手机号的包：
from phone import Phone
def get_info(phone):
    p = Phone()
    if len(phone) == 11:
        city = p.find(phone)
        print(city)
        print("%s %s" % (phone, city['city']))

if __name__ == '__main__':
    phone = 'xxxxxxxxx'
    get_info(phone)
