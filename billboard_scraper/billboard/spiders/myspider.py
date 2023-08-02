import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com']

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links:
            print(link)