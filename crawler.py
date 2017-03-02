import requests
from bs4 import BeautifulSoup
# import lxml

mangaUrl = 'http://www.mangatown.com/manga/boku_no_hero_academia/'
res = requests.get(mangaUrl)

file = open("temp.txt","w")
file.write(res.content)
file.close()


# soup = BeautifulSoup(res.text,'lxml')
soup = BeautifulSoup(res.content,'html.parser')

chapterList = soup.find('ul',{'class':'chapter_list'})
# file = open("output.txt","wb")
# for chapter in chapterList.findAll('a'):
# 	url = chapter['href']
# 	print url
# 	res = requests.get(url)
# 	soup = BeautifulSoup(res.content,'html.parser')
# 	picUrl = soup.find('meta',{'property':'og:image'})
# 	print picUrl['content']
	# file.write(chapter['href']+'\n')
	# url = chapter['href']
	# res = requests.get(url)
# file.close()

for title in chapterList.findAll("span",{"class":""}):
	print type(str(title.string))
