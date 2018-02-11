import requests
from bs4 import BeautifulSoup
from crawler import MangaStream as MStream



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
	chapter_url = 'https://readms.net/r/my_hero_academia/170/4882/'
	manga = MStream(manga_url)
	manga.DownloadChapter(head_title = 'hero_170.',
		page_num = 30, url = chapter_url)


if __name__ == '__main__':
	main()
