'''
这是我在一个虚拟机上建立了
一个mysql数据库，并对其进行
一些操作的过程

'''

import pymysql
import os

db = pymysql.connect('localhost','root','123456','banji')#连接数据库
# 使用 cursor() 方法创建一个游标对象 cursor)
cursor = db.cursor()
# 查询语句
sql_find = "select * from class;"
sql_find = "select 姓名 from class;"
# 执行sql语句
cursor.execute(sql_find)
# 查看(元组形式)
results = cursor.fetchall()
print(results)





'''############################################################################
由于学籍号类型被我重置了，重新更新它
li = []
for i in results:
    li.append(i[0])

cnt = 844

for i in li:
    sql_update1 = "update class set 学籍号=%d where 姓名='%s' ;"%(cnt,i)
    cursor.execute(sql_update1)
    cnt += 1

sql_find = "select * from class;"
cursor.execute(sql_find)
results = cursor.fetchall()
#print(results)
db.commit()
###############################################################################
'''

#sql_update1 = "update class set 学籍号=%s "

'''
导入数据操作
with open("1.csv",encoding='utf-8') as f:
    f = f.read()
    f = f.split('\n')
li = []
for i in f:
    ans = i.split()
    li.append(ans)

#由于表建好了第一个数据是手打的，pop两位
li.pop(0)
li.pop(0)
'''
'''
一开始添加数据用
for i in li:
    sql_insert = "insert into class values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
    cursor.execute(sql_insert)
'''
#db.commit()#提交数据，否则mysql那边不显示
#db.close()


