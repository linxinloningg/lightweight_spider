import requests
from lxml import etree
import json

class AiqiyiSpider:
    def __init__(self):
        self.url="https://www.iqiyi.com/dianying_new/i_list_paihangbang.html"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def parse_url(self):
        respone = requests.get(self.url,headers=self.headers)
        #print(respone.content.decode())
        return respone.content.decode()

    def get_content(self,html_str):

        element = etree.HTML(html_str)

        rebo_li_list = element.xpath(".//div[@class='piclist-scroll-pic']/div[@data-seq='1']/ul/li")

        gaofen_li_list = element.xpath(".//div[@class='piclist-scroll-pic']/div[@data-seq='2']/ul/li")

        rebo_list=[]
        gaofen_list=[]

        for li in rebo_li_list :
            item_rebo={}
            item_rebo["title"]=li.xpath(".//div[@class='title']/p/a/@title")
            item_rebo["title"]=item_rebo["title"][0] if len(item_rebo["title"]) > 0 else None

            item_rebo["href"]=li.xpath(".//div[@class='title']/p/a/@href")
            item_rebo["href"]=item_rebo["href"][0] if len(item_rebo["href"]) > 0 else None

            item_rebo["describe"]=li.xpath(".//p[@class='site-piclist_info_describe']/text()")
            item_rebo["describe"]=item_rebo["describe"][0] if len(item_rebo["describe"]) > 0 else None

            item_rebo["score"]=li.xpath(".//div[@class='site-title_score']/span/strong/text()")
            item_rebo["score"]=item_rebo["score"][0] if len(item_rebo["score"]) > 0 else None

            rebo_list.append(item_rebo)

        for li in gaofen_li_list :
            item_gaofen={}
            item_gaofen["title"]=li.xpath(".//div[@class='title']/p/a/@title")
            item_gaofen["title"]=item_gaofen["title"][0] if len(item_gaofen["title"]) > 0 else None

            item_gaofen["href"]=li.xpath(".//div[@class='title']/p/a/@href")
            item_gaofen["href"]=item_gaofen["href"][0] if len(item_gaofen["href"]) > 0 else None

            item_gaofen["describe"]=li.xpath(".//p[@class='site-piclist_info_describe']/text()")
            item_gaofen["describe"]=item_gaofen["describe"][0] if len(item_gaofen["describe"]) > 0 else None

            item_gaofen["score"]=li.xpath(".//div[@class='site-title_score']/span/strong/text()")
            item_gaofen["score"]=item_gaofen["score"][0] if len(item_gaofen["score"]) > 0 else None

            gaofen_list.append(item_gaofen)


        return rebo_list,gaofen_list

    def save_content(self,rebo_list,gaofen_list):
        with open(r"Aiqiyi.txt","w",encoding='utf-16') as f:
            f.write("爱奇艺热播榜\n\n\n")
            for content in rebo_list :
                print(content)
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
            f.write("\n\n\n爱奇艺高分榜\n\n\n")
            for content in gaofen_list :
                print(content)
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")



    def run(self):

        html_str = self.parse_url()
        rebo_list,gao_list = self.get_content(html_str)
        self.save_content(rebo_list,gao_list)


if __name__ == '__main__':
    AiqiyiSpider = AiqiyiSpider()
    AiqiyiSpider.run()



