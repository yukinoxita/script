import requests
url = "https://www.webturing.com/login.php"
user_id = "" 
passwd = ""
# 本passwd还需要将密码通过其网站自己的jsMD5函数加密
# 本人使用nodejs方式将密码加密，你也可以用别的方法试一试
args = {'user_id':user_id,'password':passwd}
res = requests.post(url,data=args)
# 因为请求头会自带cookie，我们获取cookie之后加入并访问签到界面即可
print(res.text)
print(res.headers['Set-Cookie'])
s = res.headers['Set-Cookie']
s = s.split(';')[0]
a = s.split("=")[0]
b = s.split("=")[1]
mycookie={a:b}
url = 'https://www.webturing.com/postFunction.php?action=sign'
res = requests.get(url,cookies=mycookie)
print(res.text)

