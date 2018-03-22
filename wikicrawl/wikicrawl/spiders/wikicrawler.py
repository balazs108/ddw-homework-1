# -*- coding: utf-8 -*-
import scrapy


class WikicrawlerSpider(scrapy.Spider):
    name = 'wikicrawler'
    allowed_domains =['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/']

    def parse(self, response):
        if 'Special' not in response.url and 'Main_Page' not in response.url and 'Portal' not in  response.url and 'Wikipedia' not in response.url and 'User_talk' not in response.url and 'User' not in response.url and 'File' not in response.url and  'File' not in response.url:
            yield {'Article title': response.css('h1.firstHeading ::text').extract(),
					'Modification date': response.css('li#footer-info-lastmod ::text').extract()}
            for subtitle in response.css('h2 > span.mw-headline'):
                yield {'sbutitle title': subtitle.css('::text').extract_first()}

        for link in response.css('a'):
            next_page = link.css('a ::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)