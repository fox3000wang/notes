
#import scrapy
import browsercookie
import requests
# from scrapy import Request

import re


def get_title(html):
    return re.findall(
        '<title>(.*?)</title>', html, flags=re.DOTALL)[0].strip()


url = 'https://www.zhihu.com/people/edit'


chrome_cookiejar = browsercookie.chrome()
response = requests.get(url)
print(response)


response = requests.get(url, cookies=chrome_cookiejar)
print(response)
