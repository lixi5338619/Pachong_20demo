from UA import *
from pyquery import PyQuery as pq
url_five = "https://www.aliexpress.com/item/Women-Blouses-2019-Fashion-Long-Sleeve-Turn-Down-Collar-Office-Shirt-Chiffon-Blouse-Shirt-Casual-Tops/{}".format("1000006816535.html?")
content = req_wudaili(url_five)
doc = pq(content)
items = doc('.detail-main')
# print(items)
name = items('h1').text()
print(name)
pingfen = items('.product-star-order.util-clearfix').text()
print(pingfen)
yuanjia = items('.p-del-price-content.notranslate span').text()
print(yuanjia)
xianjia = items('.p-current-price').text()
print(xianjia)
color_img = items('#j-sku-list-1 li a img')
img_list= []
for url in color_img:
    # print(url.attrib['href'])
    img_list.append(url.attrib['src'])
print(img_list)
xinghao = items('.p-property-item .p-item-main ul li a').text()
print(xinghao)
returnpolicy = items('.s-serve.sp-1').text()
print(returnpolicy)
list = doc('.ui-box.product-property-main')
li=list('.property-item span').text()
print(li)
pinglun_url = "https://feedback.aliexpress.com/display/productEvaluation.htm?productId=1000006816535&ownerMemberId=234730236&companyId=243854912&memberType=seller&startValidDate=&i18n=true"
ht = req_wudaili(pinglun_url)
do = pq(ht)
html = do('.feedback-list-wrap')
i = html('.feedback-list-wrap .feedback-item.clearfix').text()
print(i)
