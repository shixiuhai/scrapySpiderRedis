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

# Set settings whose default value is deprecated to a future-proof value
BOT_NAME = "scrapySpiderRedis" # Scrapy 项目名称

SPIDER_MODULES = ["scrapySpiderRedis.spiders"] # 指定 Scrapy 查找爬虫的 Python 模块列表。这里告诉 Scrapy 在 scrapySpiderRedis.spiders 模块中查找爬虫。
NEWSPIDER_MODULE = "scrapySpiderRedis.spiders" # 但指定生成新爬虫时要使用的默认模块。默认设置为 scrapySpiderRedis.spiders，因此新爬虫将默认创建在该模块中。

ROBOTSTXT_OBEY = False # 告诉 Scrapy 遵守 robots.txt 规则,False表示不遵循规则

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7" #  这个设置指定用于为请求生成唯一指纹的实现方式。这是一个与请求去重相关的高级特性，你在这里指定了版本 2.7。
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor" #  这个设置指定要使用的 Twisted 反应器（reactor）。Twisted 是 Scrapy 底层的网络引擎。这里指定了 AsyncioSelectorReactor，它将 asyncio 与 Twisted 整合，允许异步事件处理。
FEED_EXPORT_ENCODING = "utf-8" #  确保数据以 UTF-8 格式编码。

# 开启scrapy-redis支持
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # 配置调度器为redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter" # 配置去重类为redis

# 配置redis主机密码相关
REDIS_URL = 'redis://:abc123456@127.0.0.1:6379'

# 配置数据持久化
SCHEDULER_PERSIST = True # Ture表示爬虫爬取完成后不会清空爬取队列和去重指纹集合
# 是否开启重新爬取
SCHEDULER_FLUSH_ON_START = False # False表示不重新爬取,True表示会重新爬取

# 降低log等级
LOG_LEVEL = 'DEBUG'
# 是否禁用 cookies false 禁用，true不禁用
COOKIES_ENABLED = True

# 禁用重试
# RETRY_ENABLED = False

# 是否打开重试开关
RETRY_ENABLED = True 
#重试次数 
RETRY_TIMES = 2
#超时  
DOWNLOAD_TIMEOUT = 3
#重试代码
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]
# 重定向
REDIRECT_ENABLED = True
# 启用爬取 “Ajax 页面爬取”
AJAXCRAWL_ENABLED = True



