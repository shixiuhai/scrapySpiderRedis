"""_summary_
使用的代理是 https://www.haiwaidaili.net/register?Invitation_code=2962
Returns:
    _type_: _description_
"""
import requests
from scrapySpiderRedis.log import Logging
class ProxyByHaiWaiMiddleware(object):
    """_summary_
    海外IP代理
    """
    def __init__(self):
        self.logger = Logging("scrapyProxy.log").get_logger() # 使用自定义日志器
        self.proxy_url = "http://api.haiwaidaili.net/abroad?token=2fe39c76c11314b78b0c2a5d4df5046a&num=1&format=1&protocol=http&country=&state=&city=&sep=1&csep=&type=datacenter&area=US" # 海外代理的url

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        """_summary_
        修改请求构造
        Args:
            request (_type_): _description_
            spider (_type_): _description_
        """
        proxy = self.get_random_proxy()
        if proxy:
            uri = 'https://{proxy}'.format(proxy=proxy)
            self.logger.debug(' 使用代理 ' + proxy)
            request.meta['proxy'] = uri
   
class ProxyOtherMiddleware():
    """_summary_
    视频其他代理demo
    """
    def __init__(self):
        self.logger = Logging("proxy.log").get_logger() # 使用自定义日志器
        self.proxy_url = "http://url.com" # 使用其他代理

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        """_summary_
        修改请求构造
        Args:
            request (_type_): _description_
            spider (_type_): _description_
        """
        proxy = self.get_random_proxy()
        if proxy:
            uri = 'http://{proxy}'.format(proxy=proxy)
            self.logger.debug(' 使用代理 ' + proxy)
            request.meta['proxy'] = uri
