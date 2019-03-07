import requests,random,json
from lxml import etree


class WangyiMusic():
    def __init__(self,base_url):
        self.html = self.requests_url(base_url)
        self.parse_html()

    def requests_url(self,base_url):
        USER_AGENTS = [
            # opera
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            # firefox
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            # safari
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            # chrome
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            # 360
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            # taobao
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
            # 猎豹
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            # UC浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
        ]
        USER_AGENTS = random.choice(USER_AGENTS)
        headers = {
            "User-Agent": USER_AGENTS
                }
        html= requests.get(url=base_url,headers=headers).content.decode('utf-8')
        tree = etree.HTML(html)
        return tree

    def parse_html(self):
        group_num = self.html.xpath('//div[@class="blk"]')
        for group in group_num:
            group_name = group.xpath('.//a/text()')
            group_href = group.xpath('.//a/@href')
            for i,j in zip(group_name,group_href):
                full_url = "https://music.163.com"+j
                singer_html = self.requests_url(full_url)
                singer_url  = singer_html.xpath('//ul[@class="n-ltlst f-cb"]/li[position()>1]/a/@href')
                for url in singer_url:
                    url_go ='https://music.163.com'+url
                    singer_go = self.requests_url(url_go)
                    try:
                        singer_name =singer_go.xpath('//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]//a/text()')
                        print(singer_name)
                        with open('wangyiyun.txt','a+',encoding='utf-8')as f:
                            f.write(str(singer_name)+'\n')
                    except:
                        pass

if __name__ == '__main__':
    base_url = "https://music.163.com/discover/artist/cat?"
    WangyiMusic(base_url)





