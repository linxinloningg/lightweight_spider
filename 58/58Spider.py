import requests
import re


class _58Spider:
    def __init__(self):
        self.url = "http://{city_initials}.58.com/pinpaigongyu/pn/{page}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def get_url(self, city_initials):
        # 页面=总数/每页20条
        url_list = list()
        self.url.format(city_initials=city_initials, page=0)
        content = requests.get(self.url).content.decode()
        listsum = re.findall('<span class="listsum"><em>(.*)</em>条结果</span>', content)[0]

        return

    def parse_url(self, url):
        respone = requests.get(url, headers=self.headers)
        # print(respone.content.decode())
        return respone.content.decode()

    def get_content(self, html_str):
        pass

    def save_content(self):
        pass

    def run(self):
        url = self.get_url('gz', 0)
        html_str = self.parse_url(url)
        print(html_str)


if __name__ == '__main__':
    _58Spider = _58Spider()
    _58Spider.run()
