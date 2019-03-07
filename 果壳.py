from lxml import etree
import random,urllib,requests
from pyquery import  PyQuery as pq
from urllib import request

class PaIP():
    def __init__(self):
        self.proxy=[]
    def get_proxy(self):
        headers = {                 # Chrome 17.0.963.65 版本的User-Agent
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        request = urllib.request.Request("https://www.kuaidaili.com/free/inha/" + str(1), headers=headers)
        html = urllib.request.urlopen(request).read()
        content = etree.HTML(html)
        ip = content.xpath('//td[@data-title="IP"]/text()')
        port = content.xpath('//td[@data-title="PORT"]/text()')
        for i in range(len(ip)):
            for p in range(len(port)):
                if i == p:                                      #循环添加到空列表中
                    if ip[i] + ':' + port[p] not in self.proxy:
                        self.proxy.append(ip[i] + ':' + port[p])
        return self.proxy
        # print(self.proxy)

class Guoke(PaIP):
    def __init__(self,page):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        self.baseurl = "https://www.guokr.com/ask/highlight/?page={}"
        self.page = page
        # super(Guoke, self).__init__()

    def Going(self):

        for i in range(self.page):
            print(self.proxy)

            proxy = random.choice(self.proxy)
            proxy=urllib.request.ProxyHandler({"http": proxy})
            url = self.baseurl.format(i)
            response = requests.request('get',url,headers=self.headers,proxies=proxy)
            content_all = response.content.decode('utf-8')
            doc = pq(content_all)
            items = doc('.ask-list-cp li')
            name = items('.ask-list-detials h2 a').text().split(" ")
            # print(name)
            name_url = items.find('.ask-list-detials h2 a')
            url_list= []
            for url in name_url:
                # print(url.attrib['href'])
                url_list.append(url.attrib['href'])
            for j in range(20):
                data = "名字:"+name[j]+"  链接:"+url_list[j]+'\n'
                print(data)
                with open('guoke.txt','a+',encoding='utf-8')as fp:
                    fp.write(data)

# if __name__ == '__main__':
#     page = int(input("请输入要爬多少页:"))

page = int(input("请输入要爬多少页:"))
ss=PaIP()
ss.get_proxy()
gk=Guoke(1)
gk.get_proxy()
gk.Going()


