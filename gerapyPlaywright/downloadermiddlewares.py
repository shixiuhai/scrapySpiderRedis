"""_summary_
基于playwright的分布式动态渲染加入项目 https://github.com/shixiuhai/rendered-by-playwright/tree/main
Returns:
    _type_: _description_
"""
import time
from io import BytesIO
from scrapy.http import HtmlResponse
from scrapy.utils.python import global_object_name
from gerapyPlaywright.pretend import SCRIPTS as PRETEND_SCRIPTS
from gerapyPlaywright.settings import *
import urllib.parse
from twisted.internet.threads import deferToThread
from scrapySpiderRedis.log import Logging
import random
import requests

class PlaywrightMiddleware(object):
    """
    Downloader middleware handling the requests with Playwright
    """
    logger = Logging("gerapyPlaywright.log",log_level=GERAPY_PLAYWRIGHT_LOGGING_LEVEL).get_logger()
    
    def _retry(self, request, reason, spider):
        """
        get retry request
        :param request:
        :param reason:
        :param spider:
        :return:
        """
        if not self.retry_enabled:
            return
        
        retries = request.meta.get('retry_times', 0) + 1
        retry_times = self.max_retry_times
        
        if 'max_retry_times' in request.meta:
            retry_times = request.meta['max_retry_times']
        
        stats = spider.crawler.stats
        if retries <= retry_times:
            self.logger.debug("Retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})
            retryreq = request.copy()
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust
            
            if isinstance(reason, Exception):
                reason = global_object_name(reason.__class__)
            
            stats.inc_value('retry/count')
            stats.inc_value('retry/reason_count/%s' % reason)
            return retryreq
        else:
            stats.inc_value('retry/max_reached')
            self.logger.error("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})
    
    @classmethod
    def from_crawler(cls, crawler):
        """
        init the middleware
        :param crawler:
        :return:
        """
        settings = crawler.settings
        # logging_level = settings.get('GERAPY_PLAYWRIGHT_LOGGING_LEVEL', GERAPY_PLAYWRIGHT_LOGGING_LEVEL)
        # logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging_level)
        # logging.getLogger('urllib3.connectionpool').setLevel(logging_level)
        
        # init settings
        # cls.window_width = settings.get('GERAPY_PLAYWRIGHT_WINDOW_WIDTH', GERAPY_PLAYWRIGHT_WINDOW_WIDTH)
        # cls.window_height = settings.get('GERAPY_PLAYWRIGHT_WINDOW_HEIGHT', GERAPY_PLAYWRIGHT_WINDOW_HEIGHT)
        # cls.headless = settings.get('GERAPY_PLAYWRIGHT_HEADLESS', GERAPY_PLAYWRIGHT_HEADLESS)
        # cls.ignore_https_errors = settings.get('GERAPY_PLAYWRIGHT_IGNORE_HTTPS_ERRORS',
        #                                        GERAPY_PLAYWRIGHT_IGNORE_HTTPS_ERRORS)
        # cls.executable_path = settings.get('GERAPY_PLAYWRIGHT_EXECUTABLE_PATH', GERAPY_PLAYWRIGHT_EXECUTABLE_PATH)
        # cls.disable_extensions = settings.get('GERAPY_PLAYWRIGHT_DISABLE_EXTENSIONS',
        #                                       GERAPY_PLAYWRIGHT_DISABLE_EXTENSIONS)
        # cls.hide_scrollbars = settings.get('GERAPY_PLAYWRIGHT_HIDE_SCROLLBARS', GERAPY_PLAYWRIGHT_HIDE_SCROLLBARS)
        cls.mute_audio = settings.get('GERAPY_PLAYWRIGHT_MUTE_AUDIO', GERAPY_PLAYWRIGHT_MUTE_AUDIO)
        # cls.no_sandbox = settings.get('GERAPY_PLAYWRIGHT_NO_SANDBOX', GERAPY_PLAYWRIGHT_NO_SANDBOX)
        # cls.disable_setuid_sandbox = settings.get('GERAPY_PLAYWRIGHT_DISABLE_SETUID_SANDBOX',
        #                                           GERAPY_PLAYWRIGHT_DISABLE_SETUID_SANDBOX)
        # cls.disable_gpu = settings.get('GERAPY_PLAYWRIGHT_DISABLE_GPU', GERAPY_PLAYWRIGHT_DISABLE_GPU)
        cls.download_timeout = settings.get('GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT',
                                            settings.get('DOWNLOAD_TIMEOUT', GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT))
        
        # cls.screenshot = settings.get('GERAPY_PLAYWRIGHT_SCREENSHOT', GERAPY_PLAYWRIGHT_SCREENSHOT)
        # cls.pretend = settings.get('GERAPY_PLAYWRIGHT_PRETEND', GERAPY_PLAYWRIGHT_PRETEND)
        cls.sleep = settings.get('GERAPY_PLAYWRIGHT_SLEEP', GERAPY_PLAYWRIGHT_SLEEP)
        cls.retry_enabled = settings.getbool('RETRY_ENABLED')
        cls.max_retry_times = settings.getint('RETRY_TIMES')
        cls.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        cls.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
        
        return cls()
    
    def _process_request(self, request, spider):
        """
        use pyppeteer to process spider
        :param request:
        :param spider:
        :return:
        """
        playwright_meta = request.meta.get('playwright') or {}
        self.logger.debug('playwright_meta %s', playwright_meta)
        playwright_host=random.choice(GERAPY_PLAYWRIGHT_HOST_LIST) # 随机选一个节点主机
        playwright_url = "http://" + playwright_host + "/rendered_by_playwright/requests"
        json={
            "url": f"{request.url}",
            "is_block_image": True,
            "browser_type": playwright_meta["browser_type"],
            "timeout": GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT,
            "return_type": playwright_meta["return_type"]
        }
        result = requests.post(url=playwright_url,json=json).json()
        if result.get("code")==200:
            # return result.get("text")
            response = HtmlResponse(
                request.url,
                status=200,
                body=result.get("text"),
                encoding='utf-8',
                request=request
            )
        # if screenshot_result:
        #     response.meta['screenshot'] = screenshot_result
        return response
    
    def process_request(self, request, spider):
        """
        process request using pyppeteer
        :param request:
        :param spider:
        :return:
        """
        self.logger.debug('processing request %s', request)
        return deferToThread(self._process_request, request, spider)
        # return self._process_request(request, spider)
    
    def _spider_closed(self):
        pass
    
    def spider_closed(self):
        """
        callback when spider closed
        :return:
        """
        return deferToThread(self._spider_closed)
