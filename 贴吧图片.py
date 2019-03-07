import os
from lxml import etree
import requests

kw = input("请输入贴吧名称：")
pagenum = int(input("请输入要爬取多少页码："))
for i in range(pagenum):
    payload = {'kw': kw, 'pn': ((i - 1) * 50)}
    url = "https://tieba.baidu.com/f?ie=utf-8"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko)"}
    html = requests.get(url, params=payload, headers=headers).text
    xml = etree.HTML(html)
    link_list = xml.xpath("//div[@class = 't_con cleafix']//div[@class = 'threadlist_lz clearfix']/div/a/@href")
    print(link_list)
    for link in link_list:
        link = "https://tieba.baidu.com" + link
        # print(link)
        html = requests.get(link, headers=headers).text
        xml = etree.HTML(html)
        link_list = xml.xpath("//div/img[@class = 'BDE_Image']/@src")
        # print(link_list)
        # try:
        #     name = link_list[0][-8:]
        #     if not os.path.exists("./" + kw):
        #         os.mkdir("./" + kw)
        #     with open("./%s/%s" % (kw, name), "wb") as f:
        #         data = requests.get(link_list[0]).content
        #         f.write(data)
        # except:
        #     pass

