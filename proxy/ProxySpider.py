import requests


class ProxySpider:
    ip_list = list()

    def __init__(self, ip_number):
        # 如果部署在本地
        # self.apiUrl = "http://127.0.0.1:5555/random"
        # 如果部署在docker
        # 需要运行`docker ps`查看映射端口
        self.apiUrl = "http://192.168.99.100:5555/random"
        self.ip_number = ip_number

    def geturl(self):
        pass

    def parseurl(self):

        for i in range(0, self.ip_number):
            if requests.get(self.apiUrl).status_code == 200:
                ProxySpider.ip_list.append(requests.get(self.apiUrl).text.strip())
        print("+" * 50)
        print("成功获取到{}个代理ip，现已有{}个ip".format(self.ip_number, len(ProxySpider.ip_list)))

    def run(self):
        """# 先清空已存的ip列表
        ProxySpider.ip_list = list()"""
        # 再获取新的ip列表
        self.parseurl()


if __name__ == '__main__':
    ProxySpider = ProxySpider(50)
    ProxySpider.run()
    print(ProxySpider.ip_list)
