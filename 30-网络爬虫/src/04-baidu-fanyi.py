# -*- coding:utf-8 -*-
import requests
import json

# 百度翻译

if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    url = 'https://fanyi.baidu.com/sug'
    data = {'kw': 'dog'}
    response = requests.post(url, data, headers)

    obj = response.json()

    fp = open('dog.json', 'w', encoding='utf-8')
    json.dump(obj, fp, ensure_ascii=False)  # 将obj转换为json格式并写入文件

    print('done')
