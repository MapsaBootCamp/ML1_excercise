import scrapy
import pandas as pd
import os

class My_Spider(scrapy.Spider):
    name = 'goal_spider'

    def start_requests(self):
        urls = []
        # 2019 to 2021
        # for i in range(1,1506):
        for i in range(1, 2866):
            urls.append("https://www.goal.com/en/news/"+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_1)

    def parse_1(self, response):
        link_list = response.xpath(
            "//a[@class='type-featureArticle']/@href").extract()
        urls_list = []
        for i in range(len(link_list)):
            urls_list.append("https://www.goal.com"+link_list[i])

        print(urls_list)
        for url in urls_list:
            yield scrapy.Request(url=url, callback=self.parse_2)

    def parse_2(self, response):
        title_list = response.xpath(
            "//h1[@class='article_title__Kfsaf']/text()").extract()
        content_list = response.xpath(
            "//div[@class='article_teaser__1OofW']/text()").extract()
        author_list = response.xpath(
            "//div[@class='article_authorPageLink__6nbzB']/text()").extract()
        time_list = response.xpath("//time[@class='time']/text()").extract()

        data = []
        date=time_list[0].split(',')
        year=int(date[-1])
        if year>2018:
            if ('Lionel Messi' in title_list[0]) or ('Messi' in title_list[0]):
                data.append([title_list[0], author_list[0], time_list[0], content_list[0]])
        df = pd.DataFrame(data, columns=['title', 'author', 'date', 'content'])
        file_path = 'messi_news_dataset.csv'
        if not os.path.isfile(file_path):
            df.to_csv(file_path, mode='a', index=False)
        else:
            df.to_csv(file_path, mode='a',
                      index=False, header=False)
