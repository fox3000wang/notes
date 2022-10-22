# -*- coding:utf-8 -*-
import requests

if __name__ == "__main__":
    url = 'https://www.baidu.com'
    response = requests.get(url)
    apge_html = response.text
    print(apge_html)
    with open('baidu.html', 'w') as f:
        f.write(apge_html)
    print('done')
