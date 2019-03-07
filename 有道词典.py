from urllib import request,parse
import  hashlib,time,json



def getMD5(value):
    aa = hashlib.md5()
    aa.update(bytes(value,encoding="utf-8"))
    sign = aa.hexdigest()
    return sign

def fanyi():
    salt = int(time.time() *10000)
    ts = int(time.time() * 1000)
    value = "fanyideskweb" + word + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data= {
        "i":word,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":getMD5(value),
        "ts":ts,
        "bv":"5933be86204903bb334bf023bf3eb5ed",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }
    data_str = parse.urlencode(data)
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # "Accept - Encoding":"gzip, deflate, br",
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': len(data_str),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=42474381@10.168.1.241; JSESSIONID=aaawRmNTElH3Q4_wUlzKw; OUTFOX_SEARCH_USER_ID_NCOO=1959109122.590772; ___rl__test__cookies=1550905970008',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    req = request.Request(url=url,data=bytes(data_str,encoding='utf-8'),headers=headers)
    content = request.urlopen(req).read().decode('utf-8')
    content = json.loads(content)
    try:
        sss = content["translateResult"][0][0]
        ddd = content["smartResult"]["entries"]
        print('         ',sss["src"],":",sss["tgt"])
        # print('   ',str(ddd).replace('\\r\\n','…').replace("\''",''))
        for i in ddd:
            print('         ',i)
    except Exception as e:
        print(word)
    print()

if __name__ == '__main__':
    while True:
        print("--------------------欢迎使用有道词典------------------")
        word = input("请输入单词:")
        fanyi()



