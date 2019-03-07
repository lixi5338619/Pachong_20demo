import re,time
from selenium import webdriver
from UA import UserAgent,GetProxies
from lxml import etree

def req():
    url = "https://www.douyu.com/directory/all"
    driver.get(url)
    ss = driver.page_source
    tree = etree.HTML(ss)
    return tree

def douyu(tree):
    try:
        li_list = tree.xpath('//ul[@class="layout-Cover-list"]/li/div/a/div[2]')
        for li in li_list:
            home = li.xpath('./div[@class="DyListCover-info"]/h3/text()')
            fenlei = li.xpath('./div[@class="DyListCover-info"]/span/text()')
            name = li.xpath('./div[@class="DyListCover-info"]/h2/text()')
            print(name[0]+"           "+home[0]+'\n'+fenlei[0]+"            "+fenlei[1])
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    except:
        pass



page=1
# driver = webdriver.Chrome(executable_path=r'd:\Desktop\第四阶段爬虫\chromedriver.exe')
driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
tree = req()
while True:
    driver.find_element_by_class_name(' dy-Pagination-next').click()
    page+=1
    time.sleep(2)
    douyu(tree)
    print(("======================第%d页""=======================")%page)
    if re.findall('"shark-pager-next shark-pager-disable shark-pager-disable-next"',driver.page_source)!=[]:
        break

