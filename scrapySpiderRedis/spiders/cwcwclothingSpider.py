from typing import Iterable
from scrapy import Request
from scrapySpiderRedis.items import ScrapyspiderredisItem
import scrapy
from bs4 import BeautifulSoup
import re
import time

class CwcwclothingspiderSpider(scrapy.Spider):
    name = "cwcwclothingSpider"
    allowed_domains = ["cwcwclothing.com"]
    # start_urls = ["https://cwcwclothing.com"]
    sort_link_url="https://cwcwclothing.com/collections/grace-mila"
    

    # def parse(self, response):
    #     """_summary_
    #     程序开始
    #     Args:
    #         response (_type_): _description_
    #     """
    #     pass
    def start_requests(self) -> Iterable[Request]:
        """_summary_
        爬虫开始
        Returns:
            Iterable[Request]: _description_
        """
        cookies = {
            'secure_customer_sig': '',
            'localization': 'GB',
            'cart_currency': 'GBP',
            '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D',
            '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
            '_shopify_y': 'b8b7e79a-b3fb-4527-9044-57a7f0f3f85a',
            '_orig_referrer': '',
            '_landing_page': '%2Fcollections%2Fgrace-mila',
            'receive-cookie-deprecation': '1',
            '_shopify_sa_p': '',
            'shopify_pay_redirect': 'pending',
            'keep_alive': '22c4ce70-1eee-4173-a7a1-421f60ac3927',
            '_shopify_s': '809968be-f34a-4228-a097-12d0d52d5d3f',
            '_shopify_sa_t': '2024-06-20T12%3A00%3A59.537Z',
            'qab_previous_pathname': '/collections/coats',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'secure_customer_sig=; localization=GB; cart_currency=GBP; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=b8b7e79a-b3fb-4527-9044-57a7f0f3f85a; _orig_referrer=; _landing_page=%2Fcollections%2Fgrace-mila; receive-cookie-deprecation=1; _shopify_sa_p=; shopify_pay_redirect=pending; keep_alive=22c4ce70-1eee-4173-a7a1-421f60ac3927; _shopify_s=809968be-f34a-4228-a097-12d0d52d5d3f; _shopify_sa_t=2024-06-20T12%3A00%3A59.537Z; qab_previous_pathname=/collections/coats',
            'if-none-match': '"cacheable:65d53ddaa61c30f7ce0ea8f63bebedc3"',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }   
        # yield Request(url=self.sort_link_url,headers=headers,cookies=cookies,callback=self.parse_sort_links,meta={'source_list': response.url})
        
        yield Request(url=self.sort_link_url,headers=headers,cookies=cookies,callback=self.parse_sort_links)
           
    def parse_sort_links(self,response):
        """_summary_
        解析 列表页链接
        Args:
            response (_type_): _description_
        """
        # sort_list=response.meta['source_url']
        cookies = {
        'secure_customer_sig': '',
        'localization': 'GB',
        'cart_currency': 'GBP',
        '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D',
        '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
        '_shopify_y': 'b8b7e79a-b3fb-4527-9044-57a7f0f3f85a',
        '_orig_referrer': '',
        '_landing_page': '%2Fcollections%2Fgrace-mila',
        'receive-cookie-deprecation': '1',
        '_shopify_sa_p': '',
        'shopify_pay_redirect': 'pending',
        'keep_alive': '46a6144f-0309-4250-ad19-3c663805aee6',
        '_shopify_s': '809968be-f34a-4228-a097-12d0d52d5d3f',
        '_shopify_sa_t': '2024-06-20T12%3A13%3A50.106Z',
        'qab_previous_pathname': '/collections/coats/products/nice-things-waterproof-hooded-trench-coat-dark-yellow',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'secure_customer_sig=; localization=GB; cart_currency=GBP; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=b8b7e79a-b3fb-4527-9044-57a7f0f3f85a; _orig_referrer=; _landing_page=%2Fcollections%2Fgrace-mila; receive-cookie-deprecation=1; _shopify_sa_p=; shopify_pay_redirect=pending; keep_alive=46a6144f-0309-4250-ad19-3c663805aee6; _shopify_s=809968be-f34a-4228-a097-12d0d52d5d3f; _shopify_sa_t=2024-06-20T12%3A13%3A50.106Z; qab_previous_pathname=/collections/coats/products/nice-things-waterproof-hooded-trench-coat-dark-yellow',
            'if-none-match': '"cacheable:40c8c0a1f5d4911961e39e663a189d43"',
            'priority': 'u=0, i',
            'referer': 'https://cwcwclothing.com/collections/grace-mila',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
   
        # self.logger.info("=====================")
        soup = BeautifulSoup(response.text, 'html.parser')
        href_value = soup.find_all('a', class_='mobile-nav__sublist-link', href=True)
        sort_list = ["https://cwcwclothing.com" + href["href"] for href in href_value]
        # self.logger.info(sort_list)
        # self.logger.info("=====================")
        for sort_link in sort_list:
            yield Request(url=sort_link,headers=headers,cookies=cookies,callback=self.parse_data_links,meta={"sort_url":sort_link})
        
    def parse_data_links(self,response):
        """_summary_
        解析列表页地址
        Args:
            response (_type_): _description_
        """
        cookies = {
            'secure_customer_sig': '',
            'localization': 'GB',
            'cart_currency': 'GBP',
            '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D',
            '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
            '_shopify_y': 'b8b7e79a-b3fb-4527-9044-57a7f0f3f85a',
            '_orig_referrer': '',
            '_landing_page': '%2Fcollections%2Fgrace-mila',
            'receive-cookie-deprecation': '1',
            '_shopify_sa_p': '',
            'shopify_pay_redirect': 'pending',
            'keep_alive': 'f3aa934e-978a-4373-95d9-19a2d95baa38',
            '_shopify_s': '809968be-f34a-4228-a097-12d0d52d5d3f',
            '_shopify_sa_t': '2024-06-20T12%3A13%3A53.752Z',
            'qab_previous_pathname': '/collections/coats',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'secure_customer_sig=; localization=GB; cart_currency=GBP; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22CNZJ%22%2C%22reg%22%3A%22%22%7D; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=b8b7e79a-b3fb-4527-9044-57a7f0f3f85a; _orig_referrer=; _landing_page=%2Fcollections%2Fgrace-mila; receive-cookie-deprecation=1; _shopify_sa_p=; shopify_pay_redirect=pending; keep_alive=f3aa934e-978a-4373-95d9-19a2d95baa38; _shopify_s=809968be-f34a-4228-a097-12d0d52d5d3f; _shopify_sa_t=2024-06-20T12%3A13%3A53.752Z; qab_previous_pathname=/collections/coats',
            'if-none-match': '"cacheable:711dec24e547aace4ec31a4459254d14"',
            'priority': 'u=0, i',
            'referer': 'https://cwcwclothing.com/collections/coats',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        soup = BeautifulSoup(response.text, 'html.parser')
        href_value = soup.find_all('a', class_='grid-view-item__link grid-view-item__image-container full-width-link', href=True)
        data_list = ["https://cwcwclothing.com" + href["href"] for href in href_value ]
        # for href in href_value:
        #     data_list.append("https://cwcwclothing.com" + href["href"])
        self.logger.info(f"==================解析列表页地址是{data_list[0:3]}==================")
        self.logger.info(f"==================解析meta地址是{response.meta}==================")
        # return data_list
        for data_url in data_list:
            yield Request(url=data_url,headers=headers,cookies=cookies,callback=self.parse_data_res,meta=response.meta)
        
    def parse_data_res(self,response):
        """_summary_
        解析详情页
        Args:
            response (_type_): _description_
        """
        item = ScrapyspiderredisItem() # 实例化一个数据库对象
        resp=response.text
        self.logger.info(f"详情页内容是{resp[0:20]}")
        self.logger.info(f"meta内容是{response.meta}")
        title = re.search(r'<meta property="og:title" content="(.*?)">', resp).group().split('"')[-2]
        price = re.search(r'<meta property="og:price:amount" content="(.*?)">', resp).group().split('"')[-2]
        sort = response.meta["sort_url"].split("/")[-1]
        self.logger.info(f"title is {title}, price is {price}, sort is {sort}")
        # des = re.search(r'<meta property="og:description" content="(.*?)">', resp).group().split('"')[-2]
        # size_list = []
        # size_soup = BeautifulSoup(resp, 'html.parser')
        # size_value = size_soup.find('select', class_='product-form__variants no-js', id=True)
        # size_option = size_value.find_all('option')
        # for size in size_option:
        #     size_list.append(size.text)
        # img_list = []
        # img_soup = BeautifulSoup(resp, 'html.parser')
        # src_value = img_soup.find_all('img', class_='product-single__thumbnail-image', src=True)
        # for src in src_value:
        #     img_list.append("https:" + src["src"])
        # t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
        
        
            

        
    
    
    
