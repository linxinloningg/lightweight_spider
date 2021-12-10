import requests
from lxml import etree
import json
import openpyxl
import pandas as pd

class NpmSpider:
    def __init__(self):
        self.url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def parse_url(self):
        respone = requests.get(self.url, headers=self.headers)
        return respone.content.decode()

    @staticmethod
    def get_content(html_str):
        element = etree.HTML(html_str)
        data = element.xpath('//script[@type="application/json"]/text()')[0]

        content = json.loads(data)

        # 获取国外当前数据
        # result = content["component"][0]['caseOutsideList']

        # 获取国内当前数据
        result = content["component"][0]['caseList']

        return result

    @staticmethod
    def save_content(result):
        def save_ex(result, filename):
            """
            :param result:
            :param filename:
            :return:
            """
            # 创建工作簿
            wb = openpyxl.Workbook()
            # 创建工作表
            ws = wb.active
            # 设置表的标题
            ws.title = "国内疫情"
            # 写入表头
            ws.append(["省份", "累计确诊", "死亡", "治愈"])
            # 获取各省份的数据并写入
            for separatedata in result:
                data = [separatedata["area"], separatedata["confirmed"], separatedata["died"], separatedata["crued"]]
                ws.append(data)
            # 保存到excel中
            wb.save(filename + '.xlsx')

        def sava_csv(result, filename):
            """
            :param result:
            :param filename:
            :return:
            """
            data = dict()
            data.setdefault('area', list())
            data.setdefault('confirmed', list())
            data.setdefault('died', list())
            data.setdefault('crued', list())
            for separatedata in result:
                data["area"].append(separatedata["area"])
                data["confirmed"].append(separatedata["confirmed"])
                data["died"].append(separatedata["died"])
                data["crued"].append(separatedata["crued"])
            pd.DataFrame(data).to_csv(path_or_buf=filename + '.csv')

        # save_ex(result, 'data')
        sava_csv(result, 'data')

    def run(self):
        html_str = self.parse_url()
        result = self.get_content(html_str)
        self.save_content(result)


if __name__ == '__main__':
    NpmSpider = NpmSpider()
    NpmSpider.run()
