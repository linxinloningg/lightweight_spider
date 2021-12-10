import requests
import parsel
import tomd
import os
import re


class CsdnSpider:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def parse_url(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response == 404:
            return None
        return response.text

    @staticmethod
    def get_content(html):
        page = parsel.Selector(html)
        # 创建解释器
        title = page.css(".title-article::text").get()
        content = page.css("article").get()
        content = re.sub("<a.*?a>", "", content)
        content = re.sub("<br>", "", content)
        return {'title': title, 'content': content}

    @staticmethod
    def save_content(content):
        mdcontent = tomd.Tomd(content['content']).markdown
        # 转换为markdown 文件
        path = os.getcwd()  # 获取当前的目录路径
        file_name = "./passage"
        final_road = path + file_name
        try:
            os.mkdir(final_road)
            print('创建成功！')
        except Exception as e:
            print(str(e))
        with open(final_road + r"./" + content['title'] + ".md", mode="w", encoding="utf-8") as f:
            f.write("#" + content['title'])
            f.write(mdcontent)

    def run(self):
        html = self.parse_url()
        content = self.get_content(html)
        self.save_content(content)


if __name__ == '__main__':
    CsdnSpider = CsdnSpider(
        "https://blog.csdn.net/linxinloningg/article/details/107169881")

    CsdnSpider.run()