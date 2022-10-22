# https://pypi.org/project/browsercookie/
import requests
import browsercookie

#import urllib2
import urllib.request


# 打印所有的cookie
chrome_cookiejar = browsercookie.chrome()        # 获取Chrome 浏览器中的Cookie
for cookie in chrome_cookiejar:
    print(cookie)


# how to use
print('=============================================')
url = 'https://www.baidu.com'
r = requests.get(url, cookies=chrome_cookiejar)
print(r.content)
