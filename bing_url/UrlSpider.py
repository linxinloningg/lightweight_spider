import requests
import random
from lxml import etree
import json


class UrlSpider:
    def __init__(self, pagenumber, maxnumber=500):
        self.url = 'https://cn.bing.com/search?q={}&first={}'
        self.pagenumber = pagenumber
        self.maxnumber = maxnumber

    def geturl(self, querysyntax):
        # https://cn.bing.com/search?q=inurl:asp?id 公司&first=333
        urllist = list()
        for i in range(0, self.pagenumber):
            urllist.append(self.url.format(querysyntax, random.randrange(1, self.maxnumber, 10)))
        return urllist

    def parseurl(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content.decode()

    def getvalue(self, html_str):
        element = etree.HTML(html_str)
        cite_li_list = element.xpath(".//ol[@id='b_results']/li[@class='b_algo']")
        cite_list = list()
        for li in cite_li_list:
            item_cite = {"title": li.xpath("./div[@class='b_title']/h2/a/text()")[0],
                         "cite": li.xpath("./div[@class='b_title']/h2/a/@href")[0]}
            cite_list.append(item_cite)

        return cite_list

    def savevalue(self, cite_list):
        with open('urllist.txt', 'a', encoding='UTF-8') as f:
            for cite in cite_list:
                # 剔除不符合条件的
                if 'id' in cite['cite']:
                    f.write(json.dumps(cite, ensure_ascii=False))
                    f.write("\n")
        for cite in cite_list:
            if 'id' in cite['cite']:
                print("{}:{}".format(cite['title'], cite['cite']))

    def run(self):
        urllist = self.geturl('inurl:asp?id 公司')
        for url in urllist:
            print(url)
            html_str = self.parseurl(url)
            cite_list = self.getvalue(html_str)
            self.savevalue(cite_list)
            return cite_list


if __name__ == '__main__':
    UrlSpider = UrlSpider(3)
    UrlSpider.run()
