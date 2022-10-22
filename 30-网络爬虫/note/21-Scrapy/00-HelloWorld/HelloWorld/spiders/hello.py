import scrapy


class HelloSpider(scrapy.Spider):
    name = 'hello'  # 爬虫名，必须唯一
    allowed_domains = ['www.baidu.com']  # 允许爬取的域名
    start_urls = ['http://www.baidu.com/']  # 开始爬取的url

    def parse(self, response):
        print('[HelloSpider] ===============================')
        print(response.body)
        print('[HelloSpider] ===============================')
