### python一些轻量化爬虫

#### 给项目爬虫严格按照以下格式编写：

```python
class Spider:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
    
    def get_urls(self):
        ...
    
    def parse_url(self):
        ...

    @staticmethod
    def get_content(html):
        ...

    @staticmethod
    def save_content(content):
        ...

    def run(self):
        html = self.parse_url()
        content = self.get_content(html)
        self.save_content(content)
```

#### 项目列表：

* ###### 项目列表：

  * ###### 爬取同花顺股票股东信息

    * [仓库：10jqka](https://github.com/linxinloningg/lightweight_spider/tree/main/10jqka)

  * ###### 爬取58同城租房信息

    * [仓库：58](https://github.com/linxinloningg/lightweight_spider/tree/main/58)

  * ###### 爬取爱奇艺热门电影板块电影信息 

    * [仓库：aiqiyi](https://github.com/linxinloningg/lightweight_spider/tree/main/aiqiyi)

  * ######  通过设置高级搜索语法爬取必应搜索页面网址信息

    * [仓库：bing_url](https://github.com/linxinloningg/lightweight_spider/tree/main/bing_url)

  * ###### 爬取百度新冠肺炎信息

    * [仓库：coronavirus](https://github.com/linxinloningg/lightweight_spider/tree/main/coronavirus)

  *  ###### 爬取csdn文章保存成.md文件

        * [仓库：csdn](https://github.com/linxinloningg/lightweight_spider/tree/main/csdn)

  * ###### 爬取lol官网展示的所有英雄所有皮肤图片

    * [仓库：lol](https://github.com/linxinloningg/lightweight_spider/tree/main/lol)
    
  * 模拟的cc工具
  
    * [仓库 :cc](https://github.com/linxinloningg/lightweight_spider/tree/main/cc)
  
  * csdn浏览量（慎用）
  
    * [仓库:cc2csdn](https://github.com/linxinloningg/lightweight_spider/tree/main/cc2csdn)
    
  * 百度图片
  
    * [仓库:baidu-pic](https://github.com/linxinloningg/lightweight_spider/tree/main/baidu_pic)
