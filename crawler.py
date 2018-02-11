import requests
from bs4 import BeautifulSoup

class Manga(object):
	def __init__(self, main_url):
		self.main_url = main_url

	def DownloadChapter(self, head_title = '', page_num = 0, url = ''):
		pass


class MangaStream(Manga):
	def __init__(self, main_url):
		super(MangaStream, self).__init__(main_url)

	def DownloadChapter(self, head_title = '', page_num = 0, url = ''):
		for page in range(1, page_num):
			webpage = requests.get(url + '/' + str(page))
			# get the url of image in the page
			soup = BeautifulSoup(webpage.content, 'html.parser')
			image = soup.find('img', id='manga-page')
			if image is None:
				print 'no page ' + str(page)
				break
			else:
				print image['src']
				pic_content = requests.get('http:' + image['src']).content
				pic = open(str(head_title) + str(page).zfill(3) + '.png', 'wb')
				pic.write(pic_content)
				pic.close()