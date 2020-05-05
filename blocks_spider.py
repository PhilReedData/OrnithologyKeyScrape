import scrapy


class BlockSpider(scrapy.Spider):
	name = "blocks"

	def start_requests(self):
		#urls = [
		#	'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page=0',
		#	'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page=2161'
		#]
		url_root = 'https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page='
		urls = []
		for i in range(0, 2161):
			urls.append(url_root+str(i))
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for entry in response.css('div.views-row-even'):
			yield {
				'entry' : entry.css('a ::text').get(),
				'def' : entry.css('p').get()
			}

		for entry in response.css('div.views-row-odd'):
			yield {
				'entry' : entry.css('a ::text').get(),
				'def' : entry.css('p').get()
			}



