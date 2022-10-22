# -*- coding:utf-8 -*-
import requests
# 网页采集器

# UA伪装 User-Agent
if __name__ == "__main__":

    # UA伪装 对应反扒策略, 这一节的核心，是模拟浏览器的行为，入股不加则不能获取到网页
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    url = 'https://www.baidu.com/s?'
    kw = input('请输入要查询的内容: ')
    param = {'wd': kw}
    response = requests.get(url=url, params=param, headers=heads)
    apge_html = response.text
    print(apge_html)
    with open(kw + '.html', 'w', encoding='utf-8') as f:
        f.write(apge_html)
    print('done')
