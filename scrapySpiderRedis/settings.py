# Scrapy settings for scrapySpiderRedis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# BOT_NAME = "scrapySpiderRedis"

# SPIDER_MODULES = ["scrapySpiderRedis.spiders"]
# NEWSPIDER_MODULE = "scrapySpiderRedis.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapySpiderRedis (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapySpiderRedis.middlewares.ScrapyspiderredisSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapySpiderRedis.middlewares.ScrapyspiderredisDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapySpiderRedis.pipelines.ScrapyspiderredisPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

## 项目基本信息和模块设置
BOT_NAME = "scrapySpiderRedis" # Scrapy 项目名称
SPIDER_MODULES = ["scrapySpiderRedis.spiders"] # 指定 Scrapy 查找爬虫的 Python 模块列表。这里告诉 Scrapy 在 scrapySpiderRedis.spiders 模块中查找爬虫。
NEWSPIDER_MODULE = "scrapySpiderRedis.spiders" # 但指定生成新爬虫时要使用的默认模块。默认设置为 scrapySpiderRedis.spiders，因此新爬虫将默认创建在该模块中。

## 爬虫行为设置
ROBOTSTXT_OBEY = False # 告诉 Scrapy 遵守 robots.txt 规则,False表示不遵循规则

## Twisted 和 Asyncio 集成
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7" #  这个设置指定用于为请求生成唯一指纹的实现方式。这是一个与请求去重相关的高级特性，你在这里指定了版本 2.7。
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor" #  这个设置指定要使用的 Twisted 反应器（reactor）。Twisted 是 Scrapy 底层的网络引擎。这里指定了 AsyncioSelectorReactor，它将 asyncio 与 Twisted 整合，允许异步事件处理。
FEED_EXPORT_ENCODING = "utf-8" #  确保数据以 UTF-8 格式编码。

## 数据编码和日志
LOG_LEVEL = "DEBUG" # 日志级别
SAVE_LOGS = False  # 保存自定义日志到文件
LOG_ENABLED = True # 是否开启scrapy自己的日志,Ture开启,False关闭

## Redis 集成和分布式爬取设置
DUPEFILTER_CLASS = "scrapySpiderRedis.dupefilter.CustomRFPDupeFilter" # 配置去重类为redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # 配置调度器为redis
REDIS_URL = "redis://:abc123456@127.0.0.1:6379/1" # 配置redis主机密码相关;测试环境配置redis://:abc123456@127.0.0.1:6379/1,生产环境配置redis://:abc123456@127.0.0.1:6379
SCHEDULER_PERSIST = True # 中间断层数据不会丢失，会继续重新爬取
SCHEDULER_FLUSH_ON_START = True # False表示不重新爬取,True表示会重新爬取;测试环境配置True,生产环境配置False,

##  爬取行为设置
COOKIES_ENABLED = True # 是否禁用 cookies False禁用, True不禁用
RETRY_ENABLED = True # 是否打开重试开关
RETRY_TIMES = 2 #重试次数 
DOWNLOAD_TIMEOUT = 10 # 请求超时配置
CONCURRENT_REQUESTS_PER_DOMAIN = 1  # 每个域名同时处理的请求数量
CONCURRENT_REQUESTS_PER_IP = 1 # 每个IP同时处理的请求数量
CONCURRENT_REQUESTS = 100  # 每个爬虫同时处理的请求数量
REACTOR_THREADPOOL_MAXSIZE = 30 # 增加Twisted IO线程池的最大量
# CLOSESPIDER_PAGECOUNT = 10  # 当爬取页面数量达到10时自动停止爬取

## 错误处理和重试设置
RETRY_HTTP_CODES = [401, 403, 408, 500, 502, 503, 504] # 该优先级高于HTTPERROR_ALLOWED_CODES
HTTPERROR_ALLOWED_CODES = [304] # HTTPERROR_ALLOWED_CODES是一个设置，用于定义在爬取过程中哪些HTTP错误代码是被允许的，即在哪些情况下不会触发默认的错误处理逻辑而是继续处理页面。
REDIRECT_ENABLED = False # True表示可以重定向，False表示不重定向

## 深度和延迟
DEPTH_LIMIT = 0 # 配置爬取路径深度0表示不限制
AJAXCRAWL_ENABLED = False # 是否启用爬取 “Ajax 页面爬取”
DOWNLOAD_DELAY = 3  # 设置每个请求之间的延时为3秒
RANDOMIZE_DOWNLOAD_DELAY = False # 启用随机延迟 如果你设置DOWNLOAD_DELAY为3秒，并且RANDOMIZE_DOWNLOAD_DELAY为True，那么实际的下载延迟时间将在1.5秒（3 * 0.5）到4.5秒（3 * 1.5）之间随机选取。

## 数据库和中间件
MYSQL_HOST = "192.168.6.246" # mysql数据库地址
MYSQL_DATABASE = "video" # mysql数据库库名
MYSQL_USER = "root" # mysql数据库用户铭
MYSQL_PASSWORD = "xxxx" # 数据库用户密码
MYSQL_PORT = 3306 # 数据库连接端口

# pipeline 数据存储设置
ITEM_PIPELINES = {
   "scrapySpiderRedis.pipelines.MysqlPipeline": 300,
}

# 下载中间件配置,配置接入三方请求,配置代理等,配置随机请求头等 
DOWNLOADER_MIDDLEWARES = {

}

# 爬虫中间件配置
SPIDER_MIDDLEWARES = {
   
}

# 设置mongoDB相关
MONGO_URI=""
MONGO_DB=""





