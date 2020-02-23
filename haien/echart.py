import os
import re
import time
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
def main(num):
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

    '''替换关键字'''
    title = ["cityName","confirmedCount","curedCount","deadCount"]
    see = ["省级行政区","发现病例","已治愈","已死亡","市(县)"]
    dictnaru = dict(zip(title,see))

    li = text.split('{')

    li = A.sholi(text)
    ll = sorted(li,key=lambda x: Pinyin().get_pinyin(x.provinceName).split('-')[0])

    '''获取大量数据以便实现数据可视化'''

    Time = time.strftime("%Y-%m-%d-%H",time.localtime())
    print("已创建%s的文件"%(Time))
    path_p = 'C:\\Users\\HIKKI\\Desktop\\province\\'
    path_c = 'C:\\Users\\HIKKI\\Desktop\\city\\'
    name = str(num) + '.txt'
    f_p = open(path_p + name,'w',encoding='utf-8')
    f_c = open(path_c + name,'w',encoding='utf-8')
    f_p.write(Time + '\n')
    f_c.write(Time + '\n')
    f_p.write(see[0] + ' ' + see[1] + ' ' + see[2] + ' ' + see[3] + '\n')
    f_c.write(see[4] + ' ' + see[1] + ' ' + see[2] + ' ' + see[3] + '\n')
    for i in ll:
        f_p.write(i.provinceName + ' ' + i.conformCount + ' ' + i.curedCount + ' ' + i.deadCount + '\n')
    for i in ll[0].city:
        for j in i:
            f_c.write(i[j] + ' ')
        f_c.write('\n')
    
    f_c.close()
    f_p.close()
    pass

if __name__ == '__main__':
 #   main(1)
    i = 1
    while True:
        main(i)
        i += 1
        time.sleep(3600)
