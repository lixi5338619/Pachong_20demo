import requests,time,re
from lxml import etree
from UA import GetProxies,UserAgent
class ChengZi():
    def __init__(self,base_url):
        # self.headers = {
        #     "User-Agent":
        #         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        # }
        self.html = self.requests_url(base_url)
        self.parse_html()

    def requests_url(self,base_url):
        html= requests.get(url=base_url,headers=UserAgent()).content.decode('utf-8')
        tree = etree.HTML(html)
        return tree

    def parse_html(self):
        list= self.html.xpath('//div[@class="a-section review"]')
        # print(len(list))
        for li in list:
            #   title主题    score评分   date日期   review评论    reviewer评论者
            reviewer = li.xpath('./div/div/div/a/div[2]/span/text()')
            print("ID:"+reviewer)
            title = li.xpath('.//div[@class="a-section celwidget"]/div[2]/a[2]/text()')
            print("主题"+title)
            score = li.xpath('.//div[@class="a-section celwidget"]/div[2]/a/i/span/text()')
            print("评分"+score)
            review = li.xpath('.//*[@class="a-section celwidget"]/div[4]/span/text()')
            print(""+review)
            date =li.xpath('.//*[@class="a-section celwidget"]/span/text()')
            print(date)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            error = 0
            for i in range(1):
                try:
                    data = reviewer[i]+'\n'+score[i]+'      '+title[i]+'\n'+ review[i]+"           "+date[i]
                    print(data)
                except:
                    error += 1
                    if error>=10:
                        break

if __name__ == '__main__':
    base_url = "https://www.amazon.com/product-reviews/B077J3RQLK/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber={}"
    page = 0
    for i in range(1,20000):
        # now_time = time.time()
        ChengZi(base_url.format(i))
        page+=1
        print("=======================",page,"==========================")
        # new_time = time.time()
        if re.findall(r'Sorry, no reviews match your current selections',str(requests.get(url=base_url,headers=UserAgent()).content.decode('utf-8'))):
            break
