import scrapy

# to run the spider: scrapy crawl quotes from root project directory


class QuotesSpider(scrapy.Spider):
    # name of spider must be unique within a project
    name = "quotes"


    """
    Instead of the start_request method you can just add start urls
    as a class attribute and parse will be called automatically

    parse() is Scrapy’s default callback method
    """
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]


    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        # gets data from the above links and passes it to the parser function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        The parse() method usually parses the response, 
        extracting the scraped data as dicts and also 
        finding new URLs to follow and creating new requests (Request) from them.
        """
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)