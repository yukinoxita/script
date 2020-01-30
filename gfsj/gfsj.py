import os
import time
import faker
import xlwt
import re
import xlrd
from datetime import *


class ctf_member:
    ID = 0
    name = 0
    zhiwei = 0
    chenghao = 0
    senmon = 0
    point = 0
    shiai = 0

    def __init__(self, s):
        self.s = s

    def get_info(self):
        self.ID = self.s[0]
        self.name = re.findall('[A-Z]*[0-9]*',self.s[2])[0]#将前面的姓名简写提取出来
        self.zhiwei = self.s[4]
        self.chenghao = self.s[6]
        self.senmon = self.s[8]
        self.point = self.s[10]
        self.shiai = self.s[12]

    def print_all(self):
        a = "ID = " + self.ID + '\n'
        b = "Name = " + self.name + '\n'
        c = "Zhiwei = " + self.zhiwei + '\n'
        d = "chenghao = " + self.chenghao + '\n'
        e = "senmon = " +  self.senmon + '\n'
        f = "point = " + self.point + '\n'
        g = "shiai = " + self.shiai + '\n'
        return a+b+c+d+e+f+g

    def get_ID(self):
        return self.ID
    def get_name(self):
        return self.name
    def get_zhiwei(self):
        return self.zhiwei
    def get_chenghao(self):
        return self.chenghao
    def get_senmon(self):
        return self.senmon
    def get_point(self):
        return self.point
    def get_shiai(self):
        return self.shiai
    pass
def get_yes_point():
    path = ''
    y = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")
    y += '.xls'
    path += y
    a = xlrd.open_workbook(path)
    h = a.sheet_by_name('member')
    return h.col_values(5)[1:]
    pass
y_point = get_yes_point()#获取昨天的积分数
with open("", encoding='utf-8') as fo:
    fo = fo.read()
    fo = fo.split('\n')
    pass
li = []
for i in range(0, len(fo), 13):
    a = ctf_member(fo[i:i+13])
    a.get_info()
    li.append(a)

cl = ["ID","姓名","职位","称号","方向","积分","参赛次数","昨日得分","日期"]

#制作姓名对应字典
a_name = '' 
b_name = '' 
a_name = a_name.split()
b_name = b_name.split()
d = dict(zip(a_name,b_name))

#end
#创建表并定义标题的格式
excel = xlwt.Workbook(encoding='utf-8')
sheet = excel.add_sheet('member')
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = u'微软雅黑' #字体类型
font.height = 400    #字体大小   200等于excel字体大小中的10
style.font = font   #设定样式
for i in range(len(cl)-1):
    sheet.col(i).width = 256*20
sheet.col(len(cl)-1).width = 256*30
#end
#写入文件----------------------------------------------------------
for i in range(len(cl)):
    sheet.write(0,i,cl[i],style)
#定义正文的格式
m_font = xlwt.Font()
m_font.name = u'微软雅黑'
m_font.height = 300
style.font = m_font
#end
for i in range(len(li)):
    sheet.write(int(li[i].ID),0,li[i].ID,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),1,d[li[i].name],style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),2,li[i].zhiwei,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),3,li[i].chenghao,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),4,li[i].senmon,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),5,li[i].point,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),6,li[i].shiai,style)
for i in range(len(li)):
    sheet.write(int(li[i].ID),7,int(li[i].point) - int(y_point[i]),style)
#a = time.strftime("%Y-%m-%d", time.localtime())
a = date.today().strftime("%Y-%m-%d")
sheet.write(1,8,a,style)
#----------------------------------------------------------------
excel.save(""+ a + ".xls")


