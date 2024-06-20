# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ScrapyspiderredisPipeline:
#     def process_item(self, item, spider):
#         return item
    
import pymongo
import pymysql
import tldextract
from pymysql.converters import escape_string

# class UniversityinformationPipeline:
#     def process_item(self, item, spider):
#         return item

## 暂时没有写
class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        name = item.collection
        self.db[name].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
        
        


## 重写过
class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )
    
    def open_spider(self, spider):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()
        
    
    def close_spider(self, spider):
        self.db.close()
        
    
    # 定义一个是否满足插入条件的函数进行数据简单清洗
    def clean_data(slef,item:dict)->bool:
        return True
    
    def process_item(self, item, spider):
        # print(item)
        try:
            if self.clean_data(item):  # Assuming clean_data is a method you've defined
                sql = """
                    INSERT INTO {} (
                        link, title, sort, num, price, size, color, color_img,
                        intro, main_img, detail_img, sale, evaluate_num, mark,
                        seo_title, seo_intro, seo_key, status, create_time
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                """.format(item.table)
                params = (
                    item.get('link'), item.get('title'), item.get('sort'), item.get('num'),
                    item.get('price'), item.get('size'), item.get('color'), item.get('color_img'),
                    item.get('intro'), item.get('main_img'), item.get('detail_img'), item.get('sale'),
                    item.get('evaluate_num'), item.get('mark'), item.get('seo_title'), item.get('seo_intro'),
                    item.get('seo_key'), item.get('status'), item.get('create_time')
                )
                # print(sql)
                self.cursor.execute(sql, params)
                self.db.commit()
        except Exception as e:
            print(f"Error occurred: {e}")
            self.db.rollback()
        return item
