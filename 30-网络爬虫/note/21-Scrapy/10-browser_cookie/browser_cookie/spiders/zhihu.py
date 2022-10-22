import scrapy
import browsercookie
from scrapy import Request


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/edit']

    def parse(self, response):

        print('====================================================')
        print(response)

        print(response.xpath(
            'string(//span[@class="FullnameField-name"])'))
        print(response.xpath(
            'string(//span[@class="FullnameField-name"])').extract_first())

        chrome_cookiejar = browsercookie.chrome()
        #c = dict()
        # for cookie in chrome_cookiejar:

        # yield scrapy.Request(self.start_urls[0], callback=self.parse, meta={'cookiejar': 'chrome'}, cookies=c)
        # yield scrapy.Request(self.start_urls[0], callback=self.parse)
        yield scrapy.Request(self.start_urls[0], callback=self.parse, meta={'cookiejar': 'chrome'}, cookies=chrome_cookiejar)

    pass


'''
# scrapy shell

from scrapy import Request


url = 'https://www.zhihu.com/settings/profile'
fetch(Request(url, meta={'cookiejar': 'chrome'}))
# view(response)
# 调用view函数后，在浏览器中可看到如图10-13所示的页面。

response.css('div#rename-section span.name::text').extract_first()
# '硕-奶酪'
response.xpath('string(//div[@id="js-url-preview"])').extract_first()
# 'zhihu.com/people/shuo_cheese”
'''
