from pyquery import  PyQuery as pq
import requests,os

base_url= "https://www.qiushibaike.com/hot/page/1/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
            }

response = requests.request('get',base_url,headers=headers).content.decode('utf-8')
doc=pq(response)
items =doc('#content-left')

name = items('h2').text().split(' ')
content = items('.content span').text().split(' ')
dianzan = items('.stats-vote i').text().split(' ')
pinglun = items('.stats-comments i').text().split(' ')
for i in range(25):
    data = "名字: "+name[i]+"内容: "+content[i]+'\n'+"                                                       点赞:"+dianzan[i]+" 评论: "+pinglun[i]+'\n'
    print(data)
    with open("qiushi.txt","a+",encoding='utf-8')as fp:
        fp.write(data)
img_all = items('.thumb a img')
img_list =[]
for img in img_all:
    img_list.append(img.attrib['src'])
for j in img_list:
    img_url = "https:"+j
    print(img_url)
    iii = requests.request('get',img_url,headers=headers).content
    img_name=img_url[-10:]
    kw="qiushi"
    if not os.path.exists("./" + kw):
        os.mkdir("./" + kw)
    with open("./%s/%s" % (kw, img_name), "ab") as f:
        f.write(iii)
