import requests
from bs4 import BeautifulSoup
# import lxml


# file = open("output.txt","wb")
# for chapter in chapterList.findAll('a'):
# 	url = chapter['href']
# 	print url
# 	website = requests.get(url)
# 	soup = BeautifulSoup(website.content,'html.parser')
# 	picUrl = soup.find('meta',{'property':'og:image'})
# 	print picUrl['content']
	# file.write(chapter['href']+'\n')
	# url = chapter['href']
	# website = requests.get(url)
# file.close()

def DownloadAllMangaPages(chapter_url):
	for page in range(1, 25):
		webpage = requests.get(chapter_url + '/' + str(page))
		# get the url of image in the page
		soup = BeautifulSoup(webpage.content, 'html.parser')
		image = soup.find('img', id='manga-page')
		if image is None:
			print 'no page ' + str(page)
			break
		else:
			print image['src']
			pic_content = requests.get('http:' + image['src']).content
			pic = open('hero.168_' + str(page).zfill(3) + '.png', 'wb')
			pic.write(pic_content)
			pic.close()


	# output the content of the first page of this chapter
	file = open("chapter.html","w")
	file.write(webpage.content)
	file.close()


def TestToGetAllChapterURL(manga_url):
	website = requests.get(manga_url)

	# output file
	file = open("chapter_list.html","w")
	file.write(website.content)
	file.close()


	# get all url of every chapter of manga
	soup = BeautifulSoup(website.content,'html.parser')
	chapterList = soup.find('ul',{'class':'chapters'})
	for chapter in chapterList.findAll("h5",{"class":"chapter-title-rtl"}):
		a = chapter.find("a")
		print a['href']

def main():
	manga_url = 'http://manga.fascans.com/manga/my-hero-academia'
	# TestToGetAllChapterURL(manga_url)

	# to test showing the URL of all pages
	chapter_url = 'https://readms.net/r/my_hero_academia/168/4850'
	ShowAllMangaPages(chapter_url)


if __name__ == '__main__':
	main()
