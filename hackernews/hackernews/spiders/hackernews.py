import scrapy
import datetime
import time

class hackerCrawler(scrapy.Spider):
    name = 'hackernews'
    

    # function 1
    def start_requests(self):
        self.index = 0

        base = 'https://news.ycombinator.com/'

        print('**'*50)
        yield scrapy.Request(base, callback=self.parse)

    def parse(self, response):
        

        # path to arrow button
        nums_articles = len(response.xpath('//td[@class="title"]/a/text()').getall()) - 2

        #xpaths to data
        # xpath_main = '/html/body/center/table/tr[3]/td/table/tr[{}]/td[2]/center/a/div/@class'
        published_xpath =  response.xpath('//td[2]/span[2]/a/text()').getall()
        header_xpath =     response.xpath('//td[@class="title"]/a/text()').getall()
        link_xpath =       response.xpath('//td[@class="title"]/a/@href').getall()
        views_xpath =      response.xpath('//td[@class="subtext"]/span/text()').getall()
        comments_xpath =   response.xpath('//td[@class="subtext"]/a[3]/text()').getall()

        # function for comments; replace string and convert into int
        func_replacement = lambda x: int(x.replace('\xa0comments','')) if x != 'discuss' and x != '1\xa0comment' else 0

        for x in range(0, nums_articles):
                time.sleep(2)
                
                yield {
                    'Datetime': datetime.datetime.today(),
                    'Published': published_xpath[x],
                    'Article Header': header_xpath[x],
                    'Link': link_xpath[x],
                    'Points': views_xpath[x].replace(' points', ''),
                    'Comments': func_replacement(comments_xpath[x])
                }