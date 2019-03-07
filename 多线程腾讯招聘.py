import requests
import random,os
from pyquery import PyQuery as pq



USER_AGENTS = [
          #opera
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
         #firefox
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
          #safari
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
          #chrome
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
         #360
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
         #taobao
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
         #猎豹
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        # UC浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
USER_AGENTS=random.choice(USER_AGENTS)
headers = {
    "User-Agent":USER_AGENTS
}


from queue import Queue
import time
import threading
class Thead_craw1(threading.Thread):
    def __int__(self,i,q):
        threading.Thread.__init__(self)
        self.i=i
        self.q=q

    def get_content(self,url,kw, page):
        if not os.path.exists('centent'):
            os.makedirs('centent')
        for i in range(page):
            page = i * 10
            urlp = url.format(kw, page)
            response = requests.get(url=urlp, headers=headers).content.decode('utf-8')
            return response

    def run(self):
        while True:
            if self.q.empty():
                break
            else:
                print("当前任务%s"%self.i)
                page = self.q.get()
                print('%s取出的页面是%d'%(self.i,page))
                url = "https://hr.tencent.com/position.php?keywords={}&start={}"
                response = self.get_content(url,kw,page)
                self.get_data(response)
                print(self.i,"完成")

    def get_data(self):
        doc = pq(self.response)
        items = doc('table')
        tr = items('tr').text().split(" ")
        tr = tr[1:-2]
        for data in tr:
            data = data.split("\n")
            print("正在下载- - - - - - - - -")
            try:
                cont = (
                "岗位：  " + data[0] + "   类别：" + data[1] + "   人数：" + data[2] + "  地点：" + data[3] + "  发布时间：" + data[
                    4] + '\n')
                # with open("centent/%s.txt"%kw,'a+',encoding='utf-8')as fp:
                #     fp.write(cont)
                print(cont)
            except:
                pass



if __name__ == '__main__':
    kw = input("请输入职位名字:")
    page = int(input("请输入页码:"))
    t_starttime = time.time()
    q = Queue()
    for j in range(10):
        q.put(j)
    craw_list=[]
    craw1_names = ['a','b','c']
    for i in craw1_names:
        craw1 = Thead_craw1(i,q)
        craw1.start()
        craw_list.append(craw1)
    for threadi in craw_list:
        threadi.join()
    t_endtime = time.time()
    print('任务耗时{}'.format(t_endtime-t_starttime))

