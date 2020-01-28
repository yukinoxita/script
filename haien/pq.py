import os
import re
import requests
from bs4 import BeautifulSoup
from urllib import request
import A 
from xpinyin import Pinyin
class sho:
    provinceName = ""
    conformCount = 0
    curedCount = 0
    deadCount = 0
    city = []#里面的元素要为dict    
    def __init__(self,pn,cnc,cdc,dc):
        self.provinceName = pn
        self.conformCount = cnc
        self.curedCount = cdc
        self.deadCount = dc
    #添加几个查询方法 todo
    pass
'''获取整个数据([]中的所有东西，为完整格式)'''
url = 'https://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579578460&enterid=1579578460&from=groupmessage&isappinstalled=0'
res = request.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
js = soup.findAll('script',attrs={'id':'getAreaStat'})
ans = js[0].text
head = ans.index('[')
tail = ans[::-1].index(']') 
tail = len(ans) - tail
text = ans[head:tail]
#text = text.replace(":"," : ")

li = text.split('{')

li = A.sholi(text)
ll = sorted(li,key=lambda x: Pinyin().get_pinyin(x.provinceName).split('-')[0])

'''这个脚本用来查询实施情况:'''
print("目前情况:")
for i in ll:
    print(i.provinceName,'\n',"发现病例:",i.conformCount,'\n',"已治愈:",i.curedCount,"\n","已死亡:",i.deadCount)

