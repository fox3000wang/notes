# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class HelloworldPipeline:
    def __init__(self):
        self.f = open('items.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.f.write(content.encode('utf-8') + '\n')
        return item  # 必须返回item给引擎，引擎会交给下一个管道，否则会报错

    def close_spider(self, spider):
        self.f.close()


class JsonWriterPipeline:
    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.file.close()


class MySqlPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='scrapy',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = 'insert into hello values(%s, %s, %s)'
        self.cursor.execute(sql, (item['name'], item['age'], item['job']))
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class MongoPipeline:
    def __init__(self):
        self.connect = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.connect['scrapy']
        self.collection = self.db['items']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.connect.close()
