from urllib import request,parse
from http import cookiejar

#生成步骤
cookiejar = cookiejar.CookieJar()#实例化
processor = request.HTTPCookieProcessor()

#请求管理器
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

#创建一个浏览器对象:
opener = request.build_opener(http_handler,https_handler,processor)

def login():
    url = "http://www.renren.com/PLogin.do"
    data = {
        'email':'15936176039',
        'password':'ying5338619'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    data_str = parse.urlencode(data)

    req = request.Request(url, headers=headers,data=bytes(data_str,encoding='utf-8'))
    resopnse = opener.open(req)
    getHome()

    #获取首页
def getHome():
    url = "http://www.renren.com/436477528"
    content = opener.open(url).read().decode('utf-8')
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    login()

