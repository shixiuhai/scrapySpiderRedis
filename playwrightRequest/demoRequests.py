import requests
from urllib.parse import urlparse
def selfRequests(url:str,
                 headers:str=None,
                 proxies:dict=None,
                 cookies:dict=None,
                 playwright_host:str="127.0.0.1:9001",
                 browser_type:str="chromium",
                 timeout:int=30)->str:
    request_url = "http://" + playwright_host + "/rendered_by_playwright/requests"
    json={
        "url": f"{url}",
        "is_block_image":True,
        "browser_type": browser_type,
        "timeout": timeout,
        "return_type": "text"
    }
    if headers is not None:
        json["user_agent"]=headers['User-Agent']
    if proxies is not None:
        if "http" in proxies:
            json["proxy"]=proxies["http"]
            
    if cookies is not None:
        cookies_json = []
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        for name, value in cookies.items():
            cookie_dict = {
                'domain': domain,
                'name': name,
                'path': '/',
                'value': value,
            }
            cookies_json.append(cookie_dict)
                
        json["cookies"]=cookies_json
    
    result = requests.post(url=request_url,json=json).json()
    if result.get("code")==200:
        return result.get("text")
    
if __name__ == "__main__":
    print(selfRequests(url="https://www.xiaohongshu.com/explore/654ed925000000001b00c2bc"))
    
    
    