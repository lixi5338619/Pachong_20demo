from urllib import request,parse
import json

class Translateall():
    def __init__(self,word):
        self.word = word
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/63.0.3239.132 Safari/537.36"
        }
        self.data = {
            'f': 'auto',
            'a': 'auto',
            'w': word
        }

    def translateall(self):
        data_str = parse.urlencode(self.data)
        url = 'http://fy.iciba.com/ajax.php?a=fy'
        req=request.Request(url =url,headers= self.headers,data= bytes(data_str,encoding='utf-8'))
        response = request.urlopen(req).read().decode('utf-8')
        obj = json.loads(response)

        if obj['status']==0:
            item = obj['content']['word_mean']
            print(word,":",item)
        elif obj['status'] ==1:
            item = obj['content']['out']
            print(word,":",item)
        else:
            return word

    def run(self):
        self.translateall()

if __name__ == '__main__':
    while True:
        print("----------------欢迎使用金山词霸------------------")
        word = input("请输入单词:")
        trans=Translateall(word).run()

