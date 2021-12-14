import requests


class ProxySpider:
    ip_list = list()

    # 'http://192.168.99.100:5555/random'
    def __init__(self, ip_number, proxypool_url):
        self.proxypool_url = proxypool_url
        self.ip_number = ip_number

    def geturl(self):
        pass

    def parseurl(self):

        for i in range(0, self.ip_number):
            if requests.get(self.proxypool_url).status_code == 200:
                ProxySpider.ip_list.append(requests.get(self.proxypool_url).text.strip())
        print("+"*50)
        print("成功获取到{}个代理ip，现已有{}个ip".format(self.ip_number, len(ProxySpider.ip_list)))

    def run(self):
        """# 先清空已存的ip列表
        ProxySpider.ip_list = list()"""
        # 再获取新的ip列表
        self.parseurl()
