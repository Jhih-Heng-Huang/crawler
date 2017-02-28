import requests
from bs4 import BeautifulSoup
# import lxml

res = requests.get('http://www.mangatown.com/manga/boku_no_hero_academia/')

file = open("temp.txt","w")
file.write(res.content)
file.close()


# soup = BeautifulSoup(res.text,'lxml')
soup = BeautifulSoup(res.content,'html.parser')

mangaList = soup.find('ul',{'class':'chapter_list'})
file = open("output.txt","wb")
for line in mangaList.findAll('a'):
	url = line['href']
	print url
	res = requests.get(url)
	soup = BeautifulSoup(res.content,'html.parser')
	picUrl = soup.find('meta',{'property':'og:image'})
	print picUrl['content']
	# file.write(line['href']+'\n')
	# url = line['href']
	# res = requests.get(url)
file.close()
