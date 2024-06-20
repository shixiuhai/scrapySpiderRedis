import requests
import re
import pymysql
import time
from bs4 import BeautifulSoup

class MysqlDb:
    """
    初始化数据库，连接数据库、获取操作游标
    :return:
    """

    def __init__(self, host, user, password, database, selectReturnType='one') -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.selectReturnType = selectReturnType
        # 创建对象连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 创建连接数据库游标
        self.cursor = self.conn.cursor()

    # 定义一个关闭数据库连接的方法
    def closeConnect(self):
        self.cursor.close()
        self.conn.close()

    def executeSql(self, sql):
        """
            执行sql语句，针对读操作返回结果集
            args：
                sql  ：sql语句
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 获取所有列表记录
            results = self.cursor.fetchall()
            # 关闭数据库连接
            self.closeConnect()
            return results
        except pymysql.Error as e:
            error = '执行sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print(error)

    def executeCommit(self, sql):
        """
        执行数据库sql语句，针对更新,删除,事务等操作失败时回滚
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库
            self.conn.commit()
            # 关闭连接
            self.closeConnect()
        except pymysql.Error as e:
            self.conn.rollback()
            error = '执行数据库sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print("error:", error)

def sort_links() -> list:
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

    response = requests.get('https://cwcwclothing.com/collections/grace-mila', cookies=cookies, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    href_value = soup.find_all('a', class_='mobile-nav__sublist-link', href=True)
    sort_list = []
    for href in href_value:
        sort_list.append("https://cwcwclothing.com" + href["href"])
    return sort_list

def data_links(url: str) -> list:
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

    response = requests.get(url, cookies=cookies, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    href_value = soup.find_all('a', class_='grid-view-item__link grid-view-item__image-container full-width-link', href=True)
    data_list = []
    for href in href_value:
        data_list.append("https://cwcwclothing.com" + href["href"])
    return data_list

def data_res(url: str) -> str:
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

    response = requests.get(url,cookies=cookies,headers=headers).text
    return response

if __name__ == "__main__":
    all_sort_links = sort_links()
    for sort_link in all_sort_links:
        all_data_links = data_links(sort_link)
        for data_link in all_data_links:
            response = data_res(data_link)

            title = re.search(r'<meta property="og:title" content="(.*?)">', response).group().split('"')[-2]
            price = re.search(r'<meta property="og:price:amount" content="(.*?)">', response).group().split('"')[-2]
            sort = sort_link.split("/")[-1]
            des = re.search(r'<meta property="og:description" content="(.*?)">', response).group().split('"')[-2]
            size_list = []
            size_soup = BeautifulSoup(response, 'html.parser')
            size_value = size_soup.find('select', class_='product-form__variants no-js', id=True)
            size_option = size_value.find_all('option')
            for size in size_option:
                size_list.append(size.text)
            img_list = []
            img_soup = BeautifulSoup(response, 'html.parser')
            src_value = img_soup.find_all('img', class_='product-single__thumbnail-image', src=True)
            for src in src_value:
                img_list.append("https:" + src["src"])

            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            run_sql = "insert into cwcwclothing (`link`, `title`, `sort`, `price`, `size`, `intro`, `imgs`, `create_time`) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                    data_link, title, sort, price, str(size_list), des, str(img_list), t)
            print(run_sql)
            try:
                MysqlDb(host='127.0.0.1', user='root', password='wosuoai8279',database='crawled_outside').executeCommit(run_sql)
            except Exception as error:
                print(error)
            print(f"当前爬取的{data_link}完成！")
            time.sleep(3)

    print("当前爬取完成")
    MysqlDb(host='127.0.0.1', user='root', password='wosuoai8279', database='crawled_outside').closeConnect()
