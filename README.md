# OrnithologyKeyScrape
Web scraping '[Key to Scientific Names in Ornithology](https://www.hbw.com/dictionary/key-to-scientific-names-in-ornithology?name=&page=0)' 
before it is removed from Handbook of the Birds of the World.

1. Use Scrapy to download the dictionary content from 2,162 pages into a CSV file.
2. Convert the CSV file to an HTML file.

## 1. Use Scrapy

- Install Python and [Scrapy](https://scrapy.org/). Follow the documentation, create a new project `hbw`.
- Write [pages_spider.py](pages_spider.py) to pull out all the pages in full. (File saved in `hbw/hbw/spiders`).
- Write [blocks_spider.py](blocks_spider.py) to pull out just the dictionary entries and defintions, save to a CSV file:

```bash
scrapy crawl blocks -o blocks.csv
```

- The dictionary entries were found on two different matching CSS selectors (for the odd and even rows).
- The output is sorted with rows: Page0 odd, Page0 even, Page1 odd, Page2 even, ...

## 2. Convert CSV to HTML

- Extra Python script [extra.py](extra.py) loads the CSV file as a Pandas dataframe.
- Use empty string for blanks, sort by the dictionary entry (case insensitive).
- Using a string for HTML head and tail, take the rows of the dataframe and create HTML for each entry.
- Write the output to an HTML file with a table.
