# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes_link_follow"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }

#         next_page = response.css('li.next a::attr(href)').extract_first()

#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)



"""
Now, after extracting the data, the parse() method looks for the link to the
next page, builds a full absolute URL using the urljoin() method (since the
links can be relative) and yields a new request to the next page, registering
itself as callback to handle the data extraction for the next page and to keep
the crawling going through all the pages. 
"""


""" 
What you see here is Scrapy’s mechanism of following links: when you yield
a Request in a callback method, Scrapy will schedule that request to be sent
and register a callback method to be executed when that request finishes. 
"""


# a shortcut for the above
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_link_follow"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



# For <a> elements there is a shortcut: response.follow uses their href
# attribute automatically. So the code can be shortened further:

# for a in response.css('li.next a'):
#     yield response.follow(a, callback=self.parse)

