from requests import get
from random import randint
from bs4 import BeautifulSoup


class PageCrawl:
    def __init__(self, home_url, headers, page_num):
        """
        获取CSDN主页全部文章链接
        :param home_url: 主页url（https://blog.csdn.net/linxinloningg）
        :param headers: 随机发送请求头
        :param page_num: 页面数
        """
        self.url = home_url
        self.headers = headers
        self.page_num = page_num

    def get_urls(self):
        """
        根据页面数构造爬取页urls
        :return:
        """
        urls = list()
        for page in range(self.page_num):
            urls.append("{0}/article/list/{1}".format(self.url, page + 1))
        return urls

    def get_article_urls(self, urls):
        """
        爬取每一个页面url，获取其中的文章链接
        :param urls:
        :return:
        """
        article_urls = list()
        for page_url in urls:
            try:
                response = get(page_url, headers={"User-Agent": self.headers[randint(0, len(self.headers) - 1)],
                                                  'referer': 'http://blog.csdn.net'})
                soup = BeautifulSoup(response.content, 'lxml')
                h4 = soup.find_all("h4")
                for h in h4:
                    if h is not None:
                        article_urls.append(h.a["href"])
                    else:
                        pass
            except Exception:
                continue

        return article_urls

    def run(self):
        """
        执行函数
        :return:
        """
        return self.get_article_urls(self.get_urls())
