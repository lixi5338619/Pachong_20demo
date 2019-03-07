
from selenium import webdriver
import time
import requests
import re
driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
from UA import UserAgent
base_url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start={}"
for i in range(120):
    driver.get(base_url.format(i*15))
    ss=driver.page_source
    item = re.findall(r'class="item-root".*?</span>',ss,re.S)
    name = re.findall(r'class="title-text">(.*?)</a></div>',str(item),re.S)
    # print((name))
    href = re.findall(r'<div class="title"><a href="(.*?)" data-moreurl=',str(item),re.S)
    # print((href))
    star = re.findall(r'<span class="rating_nums">(.*?)</span>',str(ss),re.S)
    # print(star)
    for i,j,o in zip(name,href,star):
        print("----")
        content= "书名:",i," 链接:",j," 评分:",o
        with open('doubanbook.txt','w',encoding='utf-8')as f:
            f.write(str(content))





# driver.save_screenshot('kaixin1.png')
# driver.find_element_by_id('userinput').send_keys('15936176039')
# driver.find_element_by_id('passwordinput').send_keys('ying5338619')
# driver.save_screenshot('kaixin2.png')
# driver.find_element_by_id('btn_dl').click()
# time.sleep(3)
# driver.save_screenshot('kaixin3.png')
