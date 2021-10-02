import scrapy


class MessiSpider(scrapy.Spider):
    name = 'messi'

    start_urls = [
        f'https://www.goal.com/en/player/lionel-messi/{i}/c5ryhn04g9goikd0blmh83aol' for i in range(1, 53)  #53
    ]

    def parse(self, response):
        for article in response.css('article'):
            link = article.css('a::attr("href")').get()
            yield response.follow(link, self.page_parse)

    def page_parse(self, response):
        content = []
        for p in response.css('p'):
            content.append(''.join(p.css('::text').getall()))
        yield {
            'date' : response.css('time::text').get(),
            'title'    : response.css('h1::text').get(),
            'url'    : response.url,
            'content': '\n'.join(content)
            }



