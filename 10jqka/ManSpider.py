import requests
from lxml import etree
import os
import pandas as pd


class ManSpider:
    def __init__(self):
        self.url = "http://stockpage.10jqka.com.cn/{}/company/#manager"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}

    def get_urls(self, code_file_path):
        code_df = pd.read_csv(code_file_path)
        urls_dict = dict()
        for code in code_df['code']:
            code = (6 - len(str(code))) * "0" + str(code)
            urls_dict.setdefault(code, self.url.format(code))
        return urls_dict

    def parse_url(self, url):
        respone = requests.get(url, headers=self.headers)
        respone.encoding = 'utf-8'
        return respone.text

    def get_content(self, html_str):
        content = dict()
        content.setdefault("name", list())
        content.setdefault("jobs", list())
        content.setdefault("gender", list())
        content.setdefault("age", list())
        element = etree.HTML(html_str)
        divs = element.xpath('//div[@id="ml_001"]//div[contains(@class, "person_table")]')

        for div in divs:
            try:
                name = div.xpath('.//thead/tr/td/h3/a/text()')[0].replace(',', '-')
            except Exception:
                continue
            content['name'].append(name)
            try:
                jobs = div.xpath('.//thead/tr[1]/td[2]/text()')[0].replace(',', '/')
            except Exception:
                jobs = 'Null'
            content['jobs'].append(jobs)
            try:
                gender = div.xpath('.//thead/tr[2]/td[1]/text()')[0].split()[0]
            except Exception:
                gender = 'Null'
            content['gender'].append(gender)
            try:
                age = div.xpath('.//thead/tr[2]/td[1]/text()')[0].split()[1].strip('岁')
            except Exception:
                age = 'Null'
            content['age'].append(age)
        return content

    @staticmethod
    def get_content_local(html_str):
        content = dict()
        content.setdefault("name", list())
        content.setdefault("jobs", list())
        content.setdefault("gender", list())
        content.setdefault("age", list())
        element = etree.HTML(html_str)
        divs = element.xpath('//div[@id="ml_001"]//div[contains(@class, "person_table")]')

        for div in divs:
            try:
                name = div.xpath('.//thead/tr/td/h3/a/text()')[0].replace(',', '-')
            except Exception:
                continue
            content['name'].append(name)
            try:
                jobs = div.xpath('.//thead/tr[1]/td[2]/text()')[0].replace(',', '/')
            except Exception:
                jobs = 'Null'
            content['jobs'].append(jobs)
            try:
                gender = div.xpath('.//thead/tr[2]/td[1]/text()')[0].split()[0]
            except Exception:
                gender = 'Null'
            content['gender'].append(gender)
            try:
                age = div.xpath('.//thead/tr[2]/td[1]/text()')[0].split()[1].strip('岁')
            except Exception:
                age = 'Null'
            content['age'].append(age)

        return content

    @staticmethod
    def save_content(content):
        content.to_csv(path_or_buf='stock_info.csv')

    def run(self):
        pages = map(lambda _: os.path.join("html_str", _), os.listdir("html_str"))
        pages = filter(lambda _: _.endswith('html'), pages)
        content = list()
        for page in pages:
            with open(page, 'r', encoding='gbk') as file_page:
                html_str = file_page.read()

            file_name = page.split('\\')[-1]
            code = file_name.split('.')[0]

            content_dict = self.get_content(html_str)
            content_dict.setdefault('code', [code for _ in range(len(content_dict['name']))])

            content.append(pd.DataFrame(content_dict))

        self.save_content(pd.concat(content))


if __name__ == "__main__":
    ManSpider = ManSpider()
    ManSpider.run()
