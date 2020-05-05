import scrapy


class PagesSpider(scrapy.Spider):
	name = "pages"

	def start_requests(self):
		#urls = [
		#	'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page=0',
		#	'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page=2161'
		#]
		url_root = 'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page='
		urls = []
		for i in range(208, 2161):
			urls.append(url_root+str(i))
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("=")[-1]
		filename = 'data/pages/page-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saves file %s') % filename



