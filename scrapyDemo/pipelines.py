# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import json
import os
from pymongo import MongoClient
mongo = MongoClient(
    host=os.environ.get('CRAWLAB_MONGO_HOST') or 'localhost',
    port=int(os.environ.get('CRAWLAB_MONGO_PORT') or 27017),
    username=os.environ.get('CRAWLAB_MONGO_USERNAME'),
    password=os.environ.get('CRAWLAB_MONGO_PASSWORD'),
    # host='172.16.40.185',
    # port=int(os.environ.get('CRAWLAB_MONGO_PORT') or 27017),
    # username='admin',
    # password='123456',
    authSource=os.environ.get('CRAWLAB_MONGO_AUTHSOURCE') or 'admin'
)
db = mongo[os.environ.get('CRAWLAB_MONGO_DB') or 'test']
col = db[os.environ.get('CRAWLAB_COLLECTION') or 'test']
task_id = os.environ.get('CRAWLAB_TASK_ID')


class ScrapydemoPipeline:
    def process_item(self, item, spider):
        item['task_id'] = '123'
        if col is not None:
            col.save(item)
        return item