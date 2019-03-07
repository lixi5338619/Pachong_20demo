from urllib import request,parse
import json

def translateall(word):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64)"
                         " AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/63.0.3239.132 Safari/537.36"}
    data = {
        'kw':word
            }
    data_str = parse.urlencode(data)
    url = 'https://fanyi.baidu.com/sug'
    req = request.Request(url = url , headers= headers, data = bytes(data_str,encoding='utf-8'))
    response = request.urlopen(req).read().decode('utf-8')
    # print(response)
    obj = json.loads(response)
    # print(obj)
    # print(obj['data'])
    for item in obj['data']:
        item = item['k']+item['v']
        print("------------------------------------------------------------------------------")
        print(item)

if __name__ == '__main__':
    while True:
        word = input("请输入单词:")
        translateall(word)


