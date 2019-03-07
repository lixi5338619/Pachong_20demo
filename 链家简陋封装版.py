import requests
from UA import UserAgent,GetProxy
from pyquery import PyQuery as pq
from lxml import etree
from urllib.error import HTTPError
#北京每个区的信息(东城到香河)
class  Lianjia():
    def __init__(self,base_url):
        self.headers ={
                "User-Agent":UserAgent()
                 }
        self.doc = self.requests_url(base_url)
        self.parse_html()
    def requests_url(self,base_url):
        html= requests.get(url=base_url,headers=self.headers,proxies=GetProxy()).content.decode('utf-8')
        doc = pq(html)
        return doc

    def request_xml(self,xml_url):
        html= requests.get(url=xml_url,headers=self.headers).content.decode('utf-8')
        docc = etree.HTML(html)
        return docc

    def parse_html(self):
        items = self.doc('.section_sub_nav')
        quyu_all = items('a').text()
        # print(quyu_all)                   #所有区域名字
        quyuurl_all = items('a')
        url_list = []
        for quyu_url in quyuurl_all:
            url_list.append(quyu_url.attrib['href'])
                                    #url_list所有区域的url
        urlurl = []
        for dange_url in url_list[0:-2]:        #url_list[0:-2] 最后url两个有毒
            pinjie_url = "https://bj.lianjia.com"+dange_url
            urlurl.append(pinjie_url)

        veritable_url =urlurl+url_list[-2:]
        # print(veritable_url)
        for real_url in veritable_url:
            with open('lx007lianjie.txt','a+',encoding='utf-8')as f:
                new = ("\n"+str(real_url).replace("https://bj.lianjia.com/ershoufang/"," 当前区域: ").replace("/"," ")+'\n')
                print(new)
                f.write(new)
                # content = requests.get(url=real_url, headers=self.headers).content.decode('utf-8')
                # html_two = etree.HTML(content)
                html_two=self.request_xml(real_url)
                html_three = html_two.xpath('//div[@class="info clear"]')
                for data_one in html_three:
                    name_one = data_one.xpath('./div[1]/a/text()')
                    name_two = data_one.xpath('./div[2]/div[1]/text()')
                    name_three = data_one.xpath('./div[3]/div/text()|./div[3]/div/a/text()')
                    name_four = data_one.xpath('./div[4]/text()')
                    name_five = data_one.xpath('./div[@class="followInfo"]/div[@class="tag"]/span/text()')
                    name_six = data_one.xpath('./div[@class="followInfo"]/div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()|./div[@class="followInfo"]/div[@class="priceInfo"]/div[@class="totalPrice"]/text()')
                    name_seven = data_one.xpath('./div[@class="followInfo"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')
                    with open('lx007lianjie.txt', 'a+', encoding='utf-8')as f:
                        f.write("------------------------------------------------------------------------------------------------------------------"+'\n')
                        print("------------------------------------------------------------------------------------------------------------------")
                        data_cool = name_one+name_two+name_three+name_four+name_five+name_six+name_seven
                        print(data_cool)
                        f.write(str(data_cool))
                        xiangqing_url = data_one.xpath('./div[1]/a/@href')[0]
                        # xiangqing_yemian= requests.get(url=xiangqing_url,headers=self.headers).content.decode('utf-8')
                        # xiangqing_xml = etree.HTML(xiangqing_yemian)
                        xiangqing_xml=self.request_xml(xiangqing_url)
                        xiangqing_one = xiangqing_xml.xpath('//div[@id="introduction"]/div[1]/div[@class="introContent"]/div[1]/div[2]/ul/li')
                        xiangqing_two = xiangqing_xml.xpath('//div[@id="introduction"]/div[1]/div[@class="introContent"]/div[2]/div[2]/ul/li')
                        for xiangqing in xiangqing_one:
                            xiangqing_three = (xiangqing.xpath('./span/text()'))
                            xiangqing_four = (xiangqing.xpath('./text()'))
                            for i,j in zip(xiangqing_three,xiangqing_four):
                                print(i,":",j)
                                ij = (i,j)
                                with open('lx007lianjie.txt', 'a+', encoding='utf-8')as f:
                                    f.write(str(ij))
                        for xiangqing1 in xiangqing_two:
                            xiangqing_five = xiangqing1.xpath('./span/text()')
                            print(xiangqing_five)
                            with open('lx007lianjie.txt', 'a+', encoding='utf-8')as f:
                                f.write(str(xiangqing_five))

if __name__ == '__main__':
    base_url = "https://bj.lianjia.com/ershoufang/chaoyang/"
    Lianjia(base_url)

