import requests
import os
import urllib
from multiprocessing.dummy import Pool as ThreadPool
path = '' 
#读取链接文件
with open(path + "url.txt") as urls:
	urls = urls.read().split()
#读取标题文件
with open(path + "title.txt") as titles:
	titles = titles.read().split()

dic = dict(zip(urls,titles))
#print(dic)

def download(url):
	try:
		os.mkdir('pic/'+ dic[url])
	except:
		print(dic[url],"is exist")
	path = 'pic/' + dic[url] + '/'
	cnt = 0
	while True:
		cnt += 1
		pic_url = url + str(cnt) + '.png'
		print(dic[url],cnt,"is downloading")
		res = requests.get(pic_url)
		# 检验是否存在某张图片(由于该网站的图片是从1开始有规律的)
		if(str(res) == "<Response [404]>"):
			print("END")
			break
		else:
			try:
				urllib.request.urlretrieve(pic_url,filename=path+str(cnt)+'.png')
			except:
				print(str(cnt)+'.png',"下载失败")#反正我没失败过
	
#这一套这么写就对了
pool = ThreadPool()
pool.map(download,urls) #参数为函数与url列表
pool.close()
pool.join()
	
