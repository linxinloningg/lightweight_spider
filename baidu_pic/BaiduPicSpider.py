import requests
import re
import os
from tqdm import tqdm


class BaiduPicSpider:
    """

    """
    def __init__(self):
        self.url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%s"

        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def get_urls(self, name, pn):
        """

        :param name:
        :param pn:
        :return:
        """
        urls = list()
        for i in range(int(pn)):
            try:
                html_str = requests.get(self.url % (name, i * 30), headers=self.headers).content.decode()
            except Exception as e:
                print(e)
                continue
            objURLs = re.findall('"objURL":"(.*?)",', html_str)
            for objURL in objURLs:
                # url = ''.join(re.findall('https:(.*?)&', objURL))
                urls.append(objURL)
        return urls

    def parse_url(self, url):
        """

        :param url:
        :return:
        """
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.content
            else:
                return None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def save_content(content, name, num):
        """

        :param content:
        :param name:
        :param num:
        :return:
        """
        try:
            with open(os.path.join(os.path.join(os.getcwd(), 'data/' + name), name + str(num) + '.jpg'), 'ab') as f:
                f.write(content)
                f.close()
        except Exception as e:
            print(e)

    def run(self, name, pn):
        file_name = os.path.join(os.getcwd(), 'data/' + name)
        if not os.path.exists(file_name):
            os.makedirs(file_name)

        urls = self.get_urls(name, pn)

        for url in tqdm(urls):
            content = self.parse_url(url)
            if content is not None:
                self.save_content(content, name, urls.index(url))
            else:
                continue


if __name__ == '__main__':
    BaiduPicSpider = BaiduPicSpider()
    n = input('请输入要爬取的图片类别：')
    p = input('请输入要爬取的图片数量？（1等于60张图片，2等于120张图片）：')
    BaiduPicSpider.run(n, p)
