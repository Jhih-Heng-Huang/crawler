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


def TestToGetAllChapterURL(manga_url):
	manga_url = 'http://manga.fascans.com/manga/my-hero-academia'
	website = requests.get(manga_url)

	# output file
	file = open("temp.html","w")
	file.write(website.content)
	file.close()


	# soup = BeautifulSoup(website.text,'lxml')
	soup = BeautifulSoup(website.content,'html.parser')
	chapterList = soup.find('ul',{'class':'chapters'})

	# get all url of every chapter of manga
	for chapter in chapterList.findAll("h5",{"class":"chapter-title-rtl"}):
		a = chapter.find("a")
		print a['href']

def main():
	pass

if __name__ == '__main__':
	main()
