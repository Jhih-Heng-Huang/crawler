import requests
from bs4 import BeautifulSoup
from crawler import MangaStream as MStream
from crawler import JaiminisBox as JBox

def main():
	manga_name = 'my_hero_academia'
	manga = MStream(manga_name)
	manga.SelectChapter()


if __name__ == '__main__':
	main()
