# scrapy-redis脚手架
## 环境
### 1. python3.11 
### 2. scrapy2.11.2
### 3. scrapy-redis0.7.3 
## 使用
### 新建一个爬虫
 scrapy genspider cwcwclothingSpider cwcwclothing.com
## 其他
### 有个弃用告警
目录在 site-packages\scrapy_redis\dupefilter.py
### 遇到有的安装后无法导入,可能是历史残留影响
1. 卸载包
pip uninstall package
2. 清除缓存
C:\Users\*\AppData\Roaming\Python\Python311\site-packages\package
3. 重新安装
pip3 install package

