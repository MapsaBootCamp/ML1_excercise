import scrapy
from datetime import date, datetime

check_date = "01/08/2021"
obj_check_date = datetime.strptime(check_date, "%d/%m/%Y")


class goal_spider(scrapy.Spider):
    name = 'goal_messi'
    start_urls = ["https://www.goal.com/en/player/lionel-messi/1/c5ryhn04g9goikd0blmh83aol"]

    def parse(self, response):

        # links = response.css("article a::attr(href)")
        for link in response.css('.card a::attr(href)'):

            yield response.follow(link.get(), callback=self.detail)

        next_page = 'https://www.goal.com/' + response.css('a.btn.btn--older.needsclick').attrib['href']
        date = response.css("time::text")[-1].get()
        obj_date = datetime.strptime(date.strip(), '%d/%m/%Y')
        if next_page is not None:
            if obj_date >= obj_check_date:
                yield response.follow(next_page, callback=self.parse)

    def detail(self, response):
        yield {
            "Title": response.css("h1.article_title__Kfsaf::text").get(),
            "Summary": response.css("div.article_teaser__1OofW::text").get(),
            "Date": response.css('.time::text').get()

        }
