# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class EastmoneyPipeline:
    def __init__(self):
        self.f = open('items.json', 'w')

    def process_item(self, item, spider):

        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        print(content)
        # self.f.write(content.encode('utf-8'))
        self.f.write(content)
        return item  # 必须返回item给引擎，引擎会交给下一个管道，否则会报错

    def close_spider(self, spider):
        self.f.close()
