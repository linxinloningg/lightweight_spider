import requests
import re


class LolSpider:
    def __init__(self):
        self.url = 'http://lol.qq.com/biz/hero/champion.js'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}

    def get_urls(self, skin_maxnum=20):
        """
        :param skin_maxnum:最大皮肤数量
        :return:
        """

        def get_hero_id(url, headers):
            """
            获取英雄id
            :return: {'266': 'Aatrox', '103': 'Ahri', '84': 'Akali'}
            """
            content = requests.get(url, verify=False, headers=headers).content
            html_str = content.decode("gbk")
            pat_js = r'"keys":(.*?),"data"'
            enc = re.compile(pat_js)
            hero_id = eval(enc.findall(html_str)[0])
            return hero_id

        hero_id = get_hero_id(self.url, self.headers)

        urls_dict = dict()
        for id, name in hero_id.items():
            url_list = list()
            for serial_num in range(skin_maxnum):
                serial_num = "0" * (3 - len(str(serial_num))) + str(serial_num)
                url = r'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + id + serial_num + '.jpg'
                url_list.append(url)
            urls_dict.setdefault(name, url_list)

        return urls_dict

    def parse_url(self, url):
        respone = requests.get(url, verify=False, headers=self.headers)
        # print(respone.content.decode())
        if respone.status_code == 404:
            return None
        else:
            return respone.content

    def get_content(self):
        pass

    def save_content(self, content, filepath):
        with open(filepath, "wb") as f:
            f.write(content)

    def run(self):
        urls_dict = self.get_urls(skin_maxnum=20)
        for name, url_list in urls_dict.items():
            for url in url_list:
                content = self.parse_url(url)
                if content is not None:
                    print("爬取：{}".format(url))
                    self.save_content(content, "./download/{}".format(name + str(url_list.index(url)) + ".jpg"))
                else:
                    continue


if __name__ == '__main__':
    LolSpider = LolSpider()
    LolSpider.run()
