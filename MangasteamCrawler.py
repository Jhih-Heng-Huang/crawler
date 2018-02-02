import manga_crawler as manga

class MangaStreamCrawler(manga.MangaCrawler):
	def __init__(self, main_url):
		super(MangaStreamCrawler, self).__init__(main_url)

	def DownloadAllPages(self, chapter_url):
		print 'manga stream url:' + chapter_url
