from urllib import request,parse
import json

base_url = "https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
           }

with open('douban.txt','a')as f:
    f.write('豆瓣电影排行\n')
    for j in range(32):
        for i in range(10):
            error = 0
            url = base_url.format(j,i * 20)
            print(url)
            req = request.Request(url=url,headers=headers)
            content = request.urlopen(req).read().decode('utf-8')
            result = json.loads(content)
            if result==[]:
                error+=1
                print("type为%s时有误"%(j),"错误数量:%s"%(error))
            for data in result:
                name = data["title"]
                # url = data["url"]
                score = data["rating"][0]
                img_url = data["cover_url"]
                try:
                    actors = data["actors"][0]
                except:
                    actors = "LX"
                ccc = "电影名:%s,评分:%s,图片链接:%s,主演:%s,\n" % (name, score, img_url, actors)
                print(ccc)
                with open('douban.txt', 'a+', encoding='utf-8') as fp:
                    fp.write(ccc)






