from typing import Iterable
import scrapy
from scrapy import Request
# from scrapy_redis.spiders import RedisSpider
from scrapySpiderRedis.items import LvItem
from scrapySpiderRedis.log import Logging
from gerapySelenium import SeleniumRequest
from scrapy.http import HtmlResponse, Response
import re


class lvSpiderBySelenium(scrapy.Spider):
    name = "lvSpiderBySelenium"
    allowed_domains = ["ctrip.com"]
    # https://vacations.ctrip.com/list/grouptravel/sc86.html?from=do&st=%E5%9B%BD%E5%A4%96&sv=%E5%9B%BD%E5%A4%96&startcity=86&p={}
    start_urls = [  
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc346.html?st=%E5%9B%BD%E5%A4%96&startcity=346&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":346},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc578.html?st=%E5%9B%BD%E5%A4%96&startcity=578&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":578},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc19.html?st=%E5%9B%BD%E5%A4%96&startcity=19&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":19},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc407.html?st=%E5%9B%BD%E5%A4%96&startcity=407&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":407},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc22.html?st=%E5%9B%BD%E5%A4%96&startcity=22&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":22},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc86.html?st=%E5%9B%BD%E5%A4%96&startcity=86&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":86},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc571.html?st=%E5%9B%BD%E5%A4%96&startcity=571&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":571},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc491.html?st=%E5%9B%BD%E5%A4%96&startcity=491&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":491},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc308.html?st=%E5%9B%BD%E5%A4%96&startcity=308&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":308},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc375.html?st=%E5%9B%BD%E5%A4%96&startcity=375&sv=%E5%9B%BD%E5%A4%96&p={}","page":40,"from_city_code":375},
                  {"url":"https://vacations.ctrip.com/list/grouptravel/sc17.html?from=do&st=%E5%9B%BD%E5%A4%96&sv=%E5%9B%BD%E5%A4%96&startcity=17&p={}","page":40,"from_city_code":17},
                  
                  ]
    # start_url="https://www.baidu.com"
    logger = Logging("lvSpiderBySelenium.log").get_logger() # 使用自定义日志器

    # 杭州、宁波、温州、嘉兴、湖州、绍兴、金华、衢州、舟山、台州、丽水
    # https://vacations.ctrip.com/list/whole/sc17.html?st=%E5%9B%BD%E5%A4%96&startcity=17&sv=%E5%9B%BD%E5%A4%96&p=2 杭州到境外
    # https://vacations.ctrip.com/list/grouptravel/sc375.html?st=%E5%9B%BD%E5%A4%96&startcity=375&sv=%E5%9B%BD%E5%A4%96 宁波到境外
    # https://vacations.ctrip.com/list/grouptravel/sc491.html?st=%E5%9B%BD%E5%A4%96&startcity=491&sv=%E5%9B%BD%E5%A4%96 温州到境外
    # https://vacations.ctrip.com/list/grouptravel/sc571.html?st=%E5%9B%BD%E5%A4%96&startcity=571&sv=%E5%9B%BD%E5%A4%96 嘉兴到境外
    # https://vacations.ctrip.com/list/grouptravel/sc86.html?st=%E5%9B%BD%E5%A4%96&startcity=86&sv=%E5%9B%BD%E5%A4%96 湖州到境外
    # https://vacations.ctrip.com/list/grouptravel/sc22.html?st=%E5%9B%BD%E5%A4%96&startcity=22&sv=%E5%9B%BD%E5%A4%96 绍兴到境外
    # https://vacations.ctrip.com/list/grouptravel/sc308.html?st=%E5%9B%BD%E5%A4%96&startcity=308&sv=%E5%9B%BD%E5%A4%96 金华到境外
    # https://vacations.ctrip.com/list/grouptravel/sc407.html?st=%E5%9B%BD%E5%A4%96&startcity=407&sv=%E5%9B%BD%E5%A4%96 衢州到境外
    # https://vacations.ctrip.com/list/grouptravel/sc19.html?st=%E5%9B%BD%E5%A4%96&startcity=19&sv=%E5%9B%BD%E5%A4%96 舟山到境外
    # https://vacations.ctrip.com/list/grouptravel/sc578.html?st=%E5%9B%BD%E5%A4%96&startcity=578&sv=%E5%9B%BD%E5%A4%96 台州到境外
    # https://vacations.ctrip.com/list/grouptravel/sc346.html?st=%E5%9B%BD%E5%A4%96&startcity=346&sv=%E5%9B%BD%E5%A4%96 丽水到境外
    
    # https://vacations.ctrip.com/list/grouptravel/sc17.html?st=%E8%B6%8A%E5%8D%97&startcity=17&sv=%E8%B6%8A%E5%8D%97&p=2 杭州到越南
    # https://vacations.ctrip.com/list/grouptravel/sc375.html?st=%E8%B6%8A%E5%8D%97&startcity=375&sv=%E8%B6%8A%E5%8D%97&p=2 宁波到越南
    # https://vacations.ctrip.com/list/grouptravel/sc571.html?st=%E8%B6%8A%E5%8D%97&startcity=571&sv=%E8%B6%8A%E5%8D%97&p=2 嘉兴到越南
    # https://vacations.ctrip.com/list/grouptravel/sc86.html?st=%E8%B6%8A%E5%8D%97&startcity=86&sv=%E8%B6%8A%E5%8D%97&p=2 湖州到越南
    # https://vacations.ctrip.com/list/grouptravel/sc22.html?st=%E8%B6%8A%E5%8D%97&startcity=22&sv=%E8%B6%8A%E5%8D%97 绍兴到越南
    # 
    def start_requests(self) -> Iterable[Request]:
        for item in self.start_urls:
            # 下面的range忘掉了，我真想给自己两巴掌
            for page in range(1,item["page"]+1):
                try:
                    self.logger.info(f"当前页码是"+str({item["url"].format(page)}))
                    yield SeleniumRequest(url=item["url"].format(page),callback=self.parse_detail_list,meta={"from_city_code":item["from_city_code"],"page":page},sleep=5)
                except Exception as error:
                    self.logger.error(f"翻页出现错误，错误原因是{error}, 错误的页面地址是{item["url"].format(page)}")
    
    def parse_detail_list(self, response:HtmlResponse):
        # <div class="list_product_box js_product_item" data-track-product-id="1930186" data-track-is-recommend="false" data-track-inner-pos="5" style="position:relative"><div class="list_product_item_border"><div class="list_product_item flex flex-row"><div class="list_product_left" style="margin-right:16px"><div class="bg-gray-skeleton" style="width:100%;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);height:100%"></div><img class="list_product_pic" src="//dimg04.c-ctrip.com/images/0304u12000dshin6kE045_C_420_420.jpg" style="width:210px;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%)" alt="华东5市+乌镇5日4晚跟团游" title="华东5市+乌镇5日4晚跟团游" loading="lazy"><p class="list_product_tip truncate" style="max-width:150px"><span class="list_product_name">跟团游</span><i class="list_product_heng"></i><span class="list_product_place">金华出发</span></p></div><div class="list_product_right" style="flex:1;width:1%;min-height:150px"><p class="list_product_title" title="华东5市+乌镇5日4晚跟团游"><span>华东5市+乌镇5日4晚跟团游</span><img src="//pic.c-ctrip.com/VacationOnlinePic/tourpic/group_travel/list/diamond_4.png" alt="4钻" style="height: 16px; padding-left: 4px; margin-bottom: -2px;"></p><p class="list_product_subtitle" title="【携程自营·枕水江南】<限时赠>一瓶茉莉&amp;文创雪糕 升级2晚5钻&amp;宿乌镇，灵山祈福&amp;梵宫自助+4正高餐标50·品御茶宴&amp;双水乡乌镇+周庄赠景交+西湖游船+留园【纯玩无购物】南京进上海出|含大交通">【携程自营·枕水江南】&lt;限时赠&gt;一瓶茉莉&amp;文创雪糕 升级2晚5钻&amp;宿乌镇，灵山祈福&amp;梵宫自助+4正高餐标50·品御茶宴&amp;双水乡乌镇+周庄赠景交+西湖游船+留园【纯玩无购物】南京进上海出|含大交通</p><div class="list_label_box"><span class="list_label_blue" title="全程不含购物店行程（DFS、老佛爷等全球知名百货及景区景点及邮轮内等非携程商家组织的购物不包括在内），无任何购物强制消费"><span>无购物</span></span><span class="list_label_blue" title="订单一经携程旅行网以书面形式确认后均默认发团（不可抗力除外）"><span>成团保障</span></span><span class="list_label_blue" title="拿去花3期免息"><span>3期免息</span></span><span class="list_label_blue" title="线路特色"><span>宫殿</span></span><span class="list_label_blue" title="特色项目"><span>寺院祈福</span></span></div><div class="list_tiny_comment_box"><span class="list_product_score"><span>4.9</span>分</span><span class="list_product_travel">已售14019人</span><span class="list_travel_comment_separator"></span><span class="list_product_comment">4211条点评</span></div><div class="flex flex-col"><div class="absolute"><p class="list_product_retail">供应商：<span class="list_container_supplier_special"><i class="list_icon_yoyo"></i>携程自营</span></p></div><div class="flex flex-col"><div class="list_sr_price_box basefix relative"><div class="list_sr_price"><dfn>￥</dfn><strong>1276</strong>起</div><div><div class="list_pricetag_container"><span class="list_pricetag_label list_pricetag_label_first">限时促销</span><span class="list_pricetag_display"><span>已减150</span></span></div></div></div></div></div></div></div></div></div>
        detail_list = response.css('div.list_product_box.js_product_item')
        count=0
        for detail_item in detail_list:
            try:
                self.logger.info(f"当前页码是"+str(response.meta["page"]))
                count=count+1
                self.logger.info(f"当前爬取了改页面第{count}个旅游团")
                
                # <span class="list_product_place">金华出发</span>
                # <p class="list_product_tip truncate" style="max-width:150px"><span class="list_product_name">跟团游</span><i class="list_product_heng"></i><span class="list_product_place">杭州出发</span></p>
                # departure_place = (re.search(r'<span class="list_product_place">(.*?)</span>', detail_item.css('.list_product_place').get()).group(1)  if detail_item.css('.list_product_place').get() is not None else "").replace("出发","") # 出发地
                departure_place = (detail_item.css('.list_product_place::text').get()).replace("出发","") # 出发地
                
                # <p class="list_product_title" title="华东5市+乌镇5日4晚跟团游"><span>华东5市+乌镇5日4晚跟团游</span><img src="//pic.c-ctrip.com/VacationOnlinePic/tourpic/group_travel/list/diamond_4.png" alt="4钻" style="height: 16px; padding-left: 4px; margin-bottom: -2px;"></p>
                # title = detail_item.css('p.list_product_title > span::text').get() # 
                title = detail_item.css('p.list_product_title span::text').getall()[-1] if len(detail_item.css('p.list_product_title span::text').getall())>0 else ""
                
                # <div class="list_sr_price"><dfn>￥</dfn><strong>1276</strong>起</div>
                price = detail_item.css('div.list_sr_price strong::text').get().strip() if detail_item.css('div.list_sr_price strong::text').get() is not None else ""

                # <div class="list_product_box js_product_item" data-track-product-id="32800390" data-track-is-recommend="false" data-track-inner-pos="2" style="position:relative"><div class="list_product_item_border"><div class="list_product_item flex flex-row"><div class="list_product_left" style="margin-right:16px"><div class="bg-gray-skeleton" style="width:100%;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);height:100%"></div><img class="list_product_pic" src="//dimg04.c-ctrip.com/images/100b0v000000k5fkx7586_C_420_420.jpg" style="width:210px;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%)" alt="金华双龙风景旅游区+诸葛八卦村+龙游石窟2日1晚私家团" title="金华双龙风景旅游区+诸葛八卦村+龙游石窟2日1晚私家团" loading="eager"><p class="list_product_tip truncate" style="max-width:150px"><span class="list_product_name">私家团</span><i class="list_product_heng"></i><span class="list_product_place">金华出发</span></p></div><div class="list_product_right" style="flex:1;width:1%;min-height:150px"><p class="list_product_title" title="金华双龙风景旅游区+诸葛八卦村+龙游石窟2日1晚私家团"><span>金华双龙风景旅游区+诸葛八卦村+龙游石窟2日1晚私家团</span><img src="//pic.c-ctrip.com/VacationOnlinePic/tourpic/group_travel/list/diamond_5.png" alt="5钻" style="height: 16px; padding-left: 4px; margin-bottom: -2px;"></p><p class="list_product_subtitle" title="【富力万达嘉华酒店/雷迪森广场酒店·40平大房间·市区商业中心】江东道教名山+双龙洞奇洞异景+水石奇观+诸葛村古建筑+龙游大型地下建筑群·专车·亲子·情侣">【富力万达嘉华酒店/雷迪森广场酒店·40平大房间·市区商业中心】江东道教名山+双龙洞奇洞异景+水石奇观+诸葛村古建筑+龙游大型地下建筑群·专车·亲子·情侣</p><div class="list_label_box"><span class="list_label_blue" title="项目类标签"><span>含接送机/站</span></span><span class="list_label_blue" title="全程不含购物店行程（DFS、老佛爷等全球知名百货及景区景点及邮轮内等非携程商家组织的购物不包括在内），无任何购物强制消费"><span>无购物</span></span><span class="list_label_blue" title="全程不推荐、不强制任何自费项目（景区景点及邮轮内等非携程商家组织的自费行为不包括在内）"><span>无自费</span></span><span class="list_label_blue" title="订单一经携程旅行网以书面形式确认后均默认发团（不可抗力除外）"><span>成团保障</span></span><span class="list_label_blue" title="线路特色"><span>石窟</span></span><span class="list_label_blue" title="特色项目"><span>古镇古村</span></span><span class="list_label_blue" title="特色项目"><span>车型可选</span></span><span class="list_label_blue" title="酒店特色"><span>自选酒店</span></span></div><div class="list_tiny_comment_box"><span class="list_product_travel">已售4人</span></div><div class="flex flex-col"><div class="absolute"><p class="list_product_retail">供应商：风景旅游</p></div><div class="flex flex-col"><div class="list_sr_price_box basefix relative"><div class="list_sr_price"><dfn>￥</dfn><strong>1620</strong>起</div></div></div></div></div></div></div></div>
                detail_id = detail_item.css('div.list_product_box.js_product_item::attr(data-track-product-id)').get()
                from_city_code=response.meta["from_city_code"]
                detail_url=f"https://vacations.ctrip.com/travel/detail/p{detail_id}?city={from_city_code}&rv=1"
                
                yield SeleniumRequest(url=detail_url,sleep=5,pretend=True,script="""document.querySelector('[id*="pkg-tab-每日行程"]')?.click() || document.querySelector('[id*="schedule-switch-1"]')?.click();""", wait_for=".mult_cale_table",meta={"departure_place":departure_place,"title":title,"price":price,"detail_url":detail_url,"page":str(response.meta["page"])},callback=self.parse_detail)
            except Exception as error:
                self.logger.error(f"解析详情列表页错误,错误原因是{error}, 出现错误的页面地址是{response.url}")
                continue
       
        
    def parse_detail(self, response:HtmlResponse):
        try:
            self.logger.info(f"当前页面的页面是: "+ str(response.meta["page"])+" ,详情页地址是："+response.url)
            # <div class="prd_num" id="grp-103803-start-startcity">出发地：金华</div>
            if response.css('.from_city::text').get():
                detail_departure_place = response.css('.from_city::text').get().strip().split("：")[1].split("(")[0]
            elif response.css('.prd_num::text').get():
                detail_departure_place = response.css('.prd_num::text').get().strip().split("：")[1].split("(")[0]
                
            if response.xpath('//span[@class="rich_content_view_20191129 total_price"]/em/text()').get():
                detail_price=response.xpath('//span[@class="rich_content_view_20191129 total_price"]/em/text()').get()
            
            # <div class="mult_cale" id="js_schedule_calendar_table"><table class="mult_cale_table"><colgroup><col class="col_1"><col class="col_2"><col class="col_3"><col class="col_4"></colgroup><tbody><tr><th>行程</th><th>用餐</th><th>景点/场馆&amp;活动</th><th>酒店</th></tr><tr class="js_scheduleItemCalendar"><td><h3>第1天</h3><p>含免费上海接机/站服务（虹桥机场/虹桥高铁站/浦东机场）-（免费行李寄存·游客服务中心）-自由活动-送至酒店——宿上海</p></td><td><div><div><p><span class="rich_content_view_20191129 ">午餐：</span></p><p><span class="rich_content_view_20191129 ">成人不含餐，儿童不含餐</span></p><p><span>当地美食推荐：<a href="//you.ctrip.com/food/2/12614475.html" target="_blank">蒋荣兴外滩汤包(黄浦捷派店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/12308820.html" target="_blank">哈灵面馆(广西北路店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/78133922.html" target="_blank">沪西老弄堂面馆(广东路店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/7511005.html" target="_blank">老正和</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/314198.html" target="_blank">德兴馆(广东路总店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/15261731.html" target="_blank">庄氏隆兴·蟹樽小笼(外滩店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/4994197.html" target="_blank">光明邨大酒家</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/12820939.html" target="_blank">老瑞福上海菜餐厅(人民广场店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/121670096.html" target="_blank">沈大成(城隍庙店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/2/136437895.html" target="_blank">国际饭店蝴蝶酥(淮海中路店)</a></span></p></div><div><p><span class="rich_content_view_20191129 ">晚餐：</span></p><p><span class="rich_content_view_20191129 ">成人不含餐，儿童不含餐</span></p></div></div></td><td><div class="cale_spot_sec"><div><i class="icon_dot"></i><span><span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#10548698" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:10548698}" data-json="{&quot;GSScenicSpotID&quot;:10548698,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;上海城隍庙道观&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">上海城隍庙道观</a></span></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#10524119" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:10524119}" data-json="{&quot;GSScenicSpotID&quot;:10524119,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;南京路步行街&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">南京路步行街</a></span></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#75611" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:75611}" data-json="{&quot;GSScenicSpotID&quot;:75611,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;外滩&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">外滩</a></span></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#75615" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:75615}" data-json="{&quot;GSScenicSpotID&quot;:75615,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;豫园&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">豫园</a></span></span></span></span></div><div><i class="icon_dot"></i><span><span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#75614" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:75614}" data-json="{&quot;GSScenicSpotID&quot;:75614,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;金茂大厦&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">金茂大厦</a></span></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#10758168" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:0,&quot;poiid&quot;:10758168}" data-json="{&quot;GSScenicSpotID&quot;:10758168,&quot;PreName&quot;:&quot;&quot;,&quot;Name&quot;:&quot;浦江游览&quot;,&quot;SuffixName&quot;:&quot;&quot;}"><a class="itinerary_sce_name">浦江游览</a></span></span></span></span></div></div></td><td><div class="cale_htl_sec"><div><div><span><a class="itinerary_hotel_item js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-1" data-trace-keyid="177081#1#13436038" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:1,&quot;poiid&quot;:13436038}" data-json="{&quot;HotelID&quot;:13436038,&quot;HotelName&quot;:&quot;上海智微世纪酒店&quot;}">上海智微世纪酒店</a></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><a class="itinerary_hotel_item js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-1" data-trace-keyid="177081#1#107012059" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:1,&quot;poiid&quot;:107012059}" data-json="{&quot;HotelID&quot;:107012059,&quot;HotelName&quot;:&quot;上海苏宁诺富特酒店&quot;}">上海苏宁诺富特酒店</a></span><span><span class="rich_content_view_20191129 ">&nbsp;或&nbsp;</span></span><span><a class="itinerary_hotel_item js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-1" data-trace-keyid="177081#1#426531" data-trace-key="grp_detail_routinepoi_expo" data-trace-value="{&quot;type&quot;:1,&quot;poiid&quot;:426531}" data-json="{&quot;HotelID&quot;:426531,&quot;HotelName&quot;:&quot;上海外高桥喜来登酒店&quot;}">上海外高桥喜来登酒店</a></span></div></div><div><div class="rich_content_view_20191129 "><font color="orange">【漫游榜单】：性价比优选，服务+地理位置</font><br><b>上海智微世纪酒店（优先居住👍）（4.6分）</b>——周边：上海迪士尼度假区8.1公里、上海野生动物园3.85公里；<br><b>上海苏宁诺富特酒店（4.6分）</b>——周边：国际马戏剧场4.41公里、上海野生动物园4.56公里、上海迪士尼度假区6.72公里；<br><b>上海外高桥喜来登酒店（4.6分）</b>——周边：高桥黄氏民宅1.14公里、高桥新城荷兰风情小镇1.75公里、上海共青森林公园5.08公里；</div></div></div></td></tr><tr class="js_scheduleItemCalendar"><td><h3>第2天</h3><p>【苏州】山塘街or平江路—留园（VIP导游专题精讲：《世遗名录·江南古典名园美学探幽》）—【乌镇】西栅夜游——宿乌镇外</p></td><td><div><div><p><span class="rich_content_view_20191129 ">早餐：</span></p><p><span class="rich_content_view_20191129 ">成人含餐，儿童不含餐</span></p><p><span class="rich_content_view_20191129 ">享用酒店早，双早房型，不占床不含早哦~</span></p></div><div><p><span class="rich_content_view_20191129 ">午餐：</span></p><p><span class="rich_content_view_20191129 ">成人不含餐，儿童不含餐</span></p><p><span>当地美食推荐：<a href="//you.ctrip.com/food/11/119406279.html" target="_blank">江醪糟</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/11/70512103.html" target="_blank">鑫震源·苏式大虾生煎(汇邻店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/11/5123655.html" target="_blank">荣阳楼(山塘街店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/11/135268376.html" target="_blank">万福兴(凤凰街店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/11/22503670.html" target="_blank">阿文蟹黄汤包(山塘街店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/11/15507396.html" target="_blank">孙盛兴奥灶面馆(山塘街店)</a></span></p></div><div><p><span class="rich_content_view_20191129 ">晚餐：</span></p><p><span class="rich_content_view_20191129 ">成人不含餐，儿童不含餐</span></p><p><span>当地美食推荐：<a href="//you.ctrip.com/food/220/127685038.html" target="_blank">锦记糕点铺</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/5618939.html" target="_blank">吴妈馄饨</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/5619054.html" target="_blank">滋啦啦油煎铺一乌镇萝卜丝饼</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/12742739.html" target="_blank">通济酱粽店</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/5617808.html" target="_blank">酱鸭店</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/6977351.html" target="_blank">默默的家</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/11844593.html" target="_blank">乌镇忆江南餐厅(西栅东门店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/8635237.html" target="_blank">75幢民宿私房菜</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/97173319.html" target="_blank">民宿16甲私房菜</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/11844589.html" target="_blank">恒盛酒家(环河路店)</a><span style="display: inline-block; margin-left: 12px;"></span><a href="//you.ctrip.com/food/220/23556795.html" target="_blank">小镇大厨私房餐厅</a></span></p></div></div></td><td><div class="cale_spot_sec"><div><i class="icon_dot"></i><span><span><span><span class="itinerary_sce_hover js_Expose_Point js_mapPointHook" id="grp-103047-schedule-poi-0" data-trace-keyid="177081#0#81719" 
            rows=response.css('tr.js_scheduleItemCalendar')
            
            # tourist_spots = []
            # for row in rows:
            #     tourist_spots+=row.css('tr.js_scheduleItemCalendar')[0].css('td:nth-child(3) div a::text').getall()
            destination_place1= response.css('.header_inner').css('a::attr(title)').getall()[-1] if len(response.css('.header_inner').css('a::attr(title)').getall())>0 else ""
            # destination_place=response.meta["title"]
            tourist_spots = [spot for row in rows for spot in row.css('tr.js_scheduleItemCalendar')[0].css('td:nth-child(3) div a::text').getall()] 
            item = LvItem()
            meta:dict=response.meta
            item["departure_place"]=meta["departure_place"]  if detail_departure_place in meta["departure_place"] else detail_departure_place # #grp-103046-schedule-switch-1
            item["title"]=meta["title"]
            item["price"]= meta["price"]  if meta["price"] == detail_price else detail_price
            item["detail_url"]=meta["detail_url"]
            item["tourist_spots"]=",".join(tourist_spots)
            item["destination_place"]= meta["title"].split("+")[0] if meta["title"] != "" else ""
            item["destination_place1"]=destination_place1
            item["day_number"] = re.search(r'(\d+)日',  meta["title"]).group(1) if re.search(r'(\d+)日', meta["title"]) else ""
            # item["day_number"]=re.search(r'\d+日\d+晚', meta["title"]).group(0) if re.search(r'\d+日\d+晚', meta["title"]) else re.search(r'\d+日', meta["title"]).group(0) if re.search(r'\d+日', meta["title"]) else ""
            item["tourist_spots_number"]=len(tourist_spots)
            yield item
        except Exception as error:
            self.logger.error(f"数据入库出现错误，错误的原因是{error}, 出现错误的页面地址是{response.url}")
            
        # print(response.meta)
            
            
        
        
