
import scrapy
from eastmoney.items import EastmoneyItem


def trim(s):
    if s is None:
        return ''
    return s.translate(str.maketrans('', '', '\r\n')).strip()
    # .encode('utf-8')


class GetarticleSpider(scrapy.Spider):

    # 爬虫名
    name = 'getArticle'

    # 允许爬取的域名
    # 这里会有坑，不能用self.offset，因为self.offset是在parse方法中定义的，而不是在spider中定义的
    allowed_domains = ['eastmoney.com']

    # 初始URL列表
    baseURL = 'https://futures.eastmoney.com/a/cqhdd_'
    offset = 1
    start_urls = [baseURL + str(offset) + '.html']

    # 重写获取url列表的方法
    # def make_requests_from_url(self, url):
    #    return scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print('GetarticleSpider start ======================================')

        node_list = response.xpath('//div[@class="text"]')
        for node in node_list:
            item = EastmoneyItem()
            item['title'] = trim(node.xpath('./p[1]/a/text()').extract_first())
            item['content'] = trim(node.xpath('./p[2]/text()').extract_first())
            item['time'] = trim(node.xpath('./p[3]/text()').extract_first())
            item['url'] = trim(node.xpath('./p[1]/a/@href').extract_first())
            # print(item['title'])
            # print(item['content'])
            # print(item['time'])
            # print(item['url'])
            # print('-----------------')
            yield item

        if self.offset <= 25:
            self.offset += 1
            url = self.baseURL + str(self.offset) + '.html'
            print('url: ' + url)
            yield scrapy.Request(url, callback=self.parse)

        #print('GetarticleSpider end ======================================')
        # pass
        node = response.xpath('//div[@class="el-form-item__content"]')
