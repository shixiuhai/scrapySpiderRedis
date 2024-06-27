# 该run.py文件用于调试使用
from scrapy import cmdline
# spiderName 是你要运行的爬虫名称
cmdline.execute("scrapy crawl spiderName".split())