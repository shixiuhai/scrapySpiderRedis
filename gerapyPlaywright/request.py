from scrapy import Request
import copy

class PlaywrightRequest(Request):
    """
    Scrapy ``Request`` subclass providing additional arguments
    """
    
    def __init__(self, url, callback=None, wait_for=None, script=None, proxy=None,
                 sleep=None, timeout=None, pretend=None, screenshot=None, meta=None, 
                 browser_type="chromium", return_type="text", *args,
                 **kwargs):
        """
        :param url: request url
        :param callback: callback
        :param wait_for: wait for some element to load, also supports dict
        :param script: script to execute
        :param proxy: use proxy for this time, like `http://x.x.x.x:x`
        :param sleep: time to sleep after loaded, override `GERAPY_PLAYWRIGHT_SLEEP`
        :param timeout: load timeout, override `GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT`
        :param pretend: pretend as normal browser, override `GERAPY_PLAYWRIGHT_PRETEND`
        :param screenshot: ignored resource types, see
                https://miyakogi.github.io/pyppeteer/_modules/pyppeteer/page.html#Page.screenshot,
                override `GERAPY_PLAYWRIGHT_SCREENSHOT`
        :param args:
        :param kwargs:
        """
        # use meta info to save args
        meta = copy.deepcopy(meta) or {}
        playwright_meta = meta.get('playwright') or {}
        
        self.wait_for = playwright_meta.get('wait_for') if playwright_meta.get('wait_for') is not None else wait_for
        self.script = playwright_meta.get('script') if playwright_meta.get('script') is not None else script
        self.sleep = playwright_meta.get('sleep') if playwright_meta.get('sleep') is not None else sleep
        self.proxy = playwright_meta.get('proxy') if playwright_meta.get('proxy') is not None else proxy
        self.pretend = playwright_meta.get('pretend') if playwright_meta.get('pretend') is not None else pretend
        self.timeout = playwright_meta.get('timeout') if playwright_meta.get('timeout') is not None else timeout
        self.screenshot = playwright_meta.get('screenshot') if playwright_meta.get(
            'screenshot') is not None else screenshot
        self.browser_type= playwright_meta.get('browser_type') if  playwright_meta.get('browser_type') is not None else browser_type
        self.return_type = playwright_meta.get('return_type') if playwright_meta.get('return_type')  is not None else return_type
        playwright_meta = meta.setdefault('playwright', {}) # 后边的修改会对meta生效
        playwright_meta['wait_for'] = self.wait_for
        playwright_meta['script'] = self.script
        playwright_meta['sleep'] = self.sleep
        playwright_meta['proxy'] = self.proxy
        playwright_meta['pretend'] = self.pretend
        playwright_meta['timeout'] = self.timeout
        playwright_meta['screenshot'] = self.screenshot
        playwright_meta['browser_type'] = self.browser_type
        playwright_meta['return_type'] = self.return_type
        
        super().__init__(url, callback, meta=meta, *args, **kwargs)
