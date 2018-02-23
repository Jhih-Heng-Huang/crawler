import re
import requests
from bs4 import BeautifulSoup

class Manga(object):
	def __init__(self, main_url):
		self.main_url = main_url

	def SelectChapter(self):
		# gen a list of the URL of the chapter
		chapts = self.GenMangaChapts()
		# select a chapter to download
		for title, url in chapts:
			index = str(chapts.index((title, url)))
			print  index + '. ' + title
		index = input('\n' + 'Select an index you want to download:')
		(title, url) = chapts[index]
		self.DownloadChapter(chapts[index])

	def DownloadChapter(self, chapt):
		(title, url) = chapt
		page_num = self.GetPageNum(url)
		for page in xrange(1,page_num + 1):
			if not self.DownloadImg(chapt, page):
				break

	def GenMangaChapts(self):
		raise NotImplementedError
	def GenTitle(self, title):
		raise NotImplementedError
	def GenRealURL(self, url):
		raise NotImplementedError
	def GetPageNum(self, url):
		raise NotImplementedError
	def DownloadImg(self, chapt, page):
		raise NotImplementedError


class MangaStream(Manga):
	def __init__(self, main_url):
		super(MangaStream, self).__init__(main_url)

	def GenMangaChapts(self):
		webpage = requests.get(self.main_url)
		soup = BeautifulSoup(webpage.content, 'html.parser')
		stack = soup.find('table',
			class_='table table-striped').find_all('a')
		chapts = list()
		for a in stack:
			title = self.GenTitle(a.contents[0])
			url = self.GenRealURL(a['href'])
			chapts.append((title, url))
		chapts.reverse()
		return chapts

	def DownloadImg(self, chapt, page):
		(title, url) = chapt
		webpage = requests.get(url + str(page))
		# get the url of image in the page
		soup = BeautifulSoup(webpage.content, 'html.parser')
		image = soup.find('img', id='manga-page')
		if image is None:
			print 'no page ' + str(page)
			return False
		else:
			print image['src']
			pic_content = requests.get('http:' + image['src']).content
			pic = open(title + '.' + str(page).zfill(3) + '.png', 'wb')
			pic.write(pic_content)
			pic.close()
			return True

	def GenTitle(self, title):
		return re.match(r'^\d*', title, 0).group()
	def GenRealURL(self, url):
		return 'https://readms.net' + re.sub(r'\d$', '', url)
	def GetPageNum(self, url):
		return 100
		