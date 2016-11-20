import scrapy

class MotivationSpider(scrapy.Spider):
        name = 'motivational spider'
        start_urls = [
            'http://www.goodreads.com/quotes/tag/inspiration?',
        ]

        def parse(self, response):
            # for quote in response.css('section.main-section').css('div.row').css('div.container').css('div.quote.masonry-brick'):
            for quote in response.xpath('//div[@class="quoteDetails "]'):
                yield {
                    'text': quote.css('div.quoteText::text').extract_first()
                }

            next_page = response.xpath('//a[@class="next_page"]/@href').extract_first()

            print "NEXT PAGE YO: ", next_page
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
