import urllib.request
import urllib.parse
import argparse
from bs4 import BeautifulSoup

def GetHtml(url):
	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 
	request = urllib.request.Request(url=url,headers=headers)
	return urllib.request.urlopen(request).read()

class BaiduAPI:
	def __init__(self,keyword):
		self.url = 'http://www.baidu.com/s?'+urllib.parse.urlencode({'wd':keyword})
	def GetUrl(self,pn):
		return self.url+"&pn=%s"%(pn)

class GoogleAPI:
	def __init__(self,keyword):
		self.url = 'http://www.google.com.hk/'

def crawler(keyword,page):
	api = BaiduAPI(keyword)
#	api = GoogleAPI(keyword)
	for pn in range(page):
		url = api.GetUrl(str(pn)+'0')
		html = GetHtml(url)
		soup = BeautifulSoup(html,"html.parser")
		result = soup.find_all('a',class_="c-showurl")
		targetUrl = []
		for i in result:
			try:
				targetUrl.append(urllib.request.urlopen(i['href']).geturl())
			except BaseException:
				pass
	print '\n'.join(targetUrl)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-s','--keyword',type=str)
	parser.add_argument('-p','--page',type=int)
	args = parser.parse_args()
	if args.keyword:
		if not args.page:
			args.page = 1
		crawler(args.keyword,args.page)
	else:
		print "input the -s 'keyword'"
