import re
#应该是可以将pq.py中的类引用到这里的，但是我不会，没去看。copy一下也能用
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

def sholi(s):
    class_list = []
    a = sho("tmp",0,0,0)
    li = s.split('{')
    flag = True
    li.pop(0)
    dic = {}
    city = {"text":1}
    title = ["cityName","confirmedCount","curedCount","deadCount"]
    for x in li:
        x1 = x.split(',')
        #print(x1)
        #print()
        title_naiyo = []
        if re.findall('"provinceName"',x) != []:
            pn = x1[0].split(":")[1][1:-1]
            cnc = x1[2].split(":")[1]
            cdc = x1[4].split(":")[1]
            dc = x1[5].split(":")[1]
            b = sho(pn,cnc,cdc,dc)
            a.city = city
            class_list.append(a)
            a = b
            dic = {}#找到一个省就初始化dic
            city = []
            continue
        for i in x1:
            #x2 = re.findall('[^},]*',i)[0]
            #print(x2)
            if re.findall(title[0],i) != []:
                title_naiyo.append(i.split(":")[1][1:-1])
            if re.findall(title[1],i) != []:
                title_naiyo.append(i.split(":")[1])
            if re.findall(title[2],i) != []:
                title_naiyo.append(i.split(":")[1])
            if re.findall(title[3],i) != []:
                xxx = i.split(":")[1]
                xxxx = re.findall('[^\]}]',xxx)[0]#去掉不必要的字符
                title_naiyo.append(xxxx)
        dic = dict(zip(title,title_naiyo))
        city.append(dic)
       # print (a.city)
       # print()
        #print (title_naiyo)

    #print(a.provinceName,a.conformCount,a.curedCount,a.deadCount,a.city)
    a.city = city
    class_list.append(a)
    class_list.pop(0)
    return class_list
   

if __name__ == '__main__':
    s = '[{"provinceName":"安徽省","provinceShortName":"安徽","confirmedCount":106,"suspectedCount":0,"curedCount":0,"deadCount":0,"comment":"","cities":[{"cityName":"阜阳","confirmedCount":21,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"合肥","confirmedCount":16,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"马鞍山","confirmedCount":10,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"铜陵","confirmedCount":9,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"芜湖","confirmedCount":9,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"亳州","confirmedCount":8,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"安庆","confirmedCount":8,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"六安","confirmedCount":4,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"滁州","confirmedCount":4,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"黄山","confirmedCount":4,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"蚌埠","confirmedCount":3,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"宿州","confirmedCount":3,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"宣城","confirmedCount":2,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"淮北","confirmedCount":2,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"淮南","confirmedCount":2,"suspectedCount":0,"curedCount":0,"deadCount":0},{"cityName":"池州","confirmedCount":1,"suspectedCount":0,"curedCount":0,"deadCount":0}]}'
    sholi(s)