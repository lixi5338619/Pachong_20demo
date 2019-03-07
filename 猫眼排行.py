#排名，电影名，主演，时间，评分。
from pyquery import  PyQuery as pq
import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
            }
url = "https://maoyan.com/board"
response = requests.request('get',url,headers=headers)

content_all = response.content.decode('utf-8')

doc = pq(content_all)
# print(doc)
items = doc('div dd')
# print(items)
paiming = items('.board-index').text().split(" ")
name = items('.name').text().split(" ")
zhuyan =items('.star').text().split(" ")
daytime =items('.releasetime').text().split(" ")
pingfen = items('.score').text().split(" ")
img_url = items('.board-img')
print(name)
url_list = []
for url in img_url:
    # print(url.attrib['data-src'])
    url_list.append(url.attrib['data-src'])
# print(type(url_list))
for i in range(10):
    data = "排名:"+paiming[i]+" 电影:"+name[i]+" "+zhuyan[i]+" "+daytime[i]+" 评分:"+pingfen[i]+" 图片链接: "+url_list[i]
    with open('maoyan.txt','a+',encoding='utf-8')as fp:
        print(data)
        fp.write(data+'\n')
    print(data)

