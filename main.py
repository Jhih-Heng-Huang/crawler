import requests
from bs4 import BeautifulSoup
from crawler import MangaStream as MStream

def main():
	manga_url = 'https://readms.net/manga/my_hero_academia'
	manga = MStream(manga_url)
	manga.SelectChapter()


if __name__ == '__main__':
	main()
