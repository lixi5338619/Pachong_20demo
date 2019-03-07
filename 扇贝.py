import requests
from lxml import etree
page = int(input("请输入页数:"))
base_url = "https://www.shanbay.com/wordlist/187711/540709/?page={}"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
            }
for i in range(1,page+1):
    url = base_url.format(i)
    response = requests.request('get',url=url,headers=headers).content.decode('utf-8')
    content = etree.HTML(response)
    name_all = content.xpath('//tr/td/strong/text()')
    # print(name_all)
    main_all = content.xpath('//tr/td[@class="span10"]/text()')
    # print(main_all)
    for j in range(20):
        try:
            data = name_all[j]+":翻译:"+main_all[j]+'\n'
            print(data)
            with open('shanbei.txt', 'a+', encoding='utf-8')as fp:
                fp.write(data)
        except:
            print("没了")



    # tr_list = content.xpath('//tr[@class="row"]')
    # for tr in tr_list:
    #     word = tr.xpath('./td/strong/text()')
    #     detail = tr.xpath('./td[@class="span10"]/text()')
    #     info = word[0]+' :'+detail[0]+'\n'
    #     print(info)
        # with open('shanbei.txt','a+',encoding='utf-8')as fp:
        #     fp.write(info)
