[Switch to English Version](readmeEnglish.md)
# 基于scrapy和scrapy-redis爬虫的脚手架
## 环境
### 1. python3.11.9
### 2. scrapy2.11.2
### 3. scrapy-redis0.7.3 
### 4. 暂时只做了在windows环境下运行,尚未测试linux下
## 使用
### 备注
* 项目默认清理了所有不必要配置，如果要运行demo请参考spidersDemo，将内部文件替换到scrapySpiderRedis内
### 开启环境
1. 安装mysql
2. 安装redis
3. 导入测试sql到mysql
4. 在settings.py里设置mysql和redis相关用户和密码
### 新建一个爬虫
```
scrapy genspider cwcwclothingSpider cwcwclothing.com
```
### 调试建议
* 涉及列表迭代的调试先区所有列表里的0元素进行调试 比如 for item in href_list[0:1] 这种迭代，因为scrapy是多线程异步的,调试完成后可以使用全局替换[0:1]为空
### 配置中间件(需要配置的中间件在middlewaresDemo可以预览)
#### 实现的中间件
* 完成了IP代理中间件scrapyProxy.proxy.ProxyByHaiWaiMiddleware
## 其他
### 项目内的中文翻译成英文
* 暂时做不动了,谁有兴趣请联系邮箱15256728901@163.com或issue
### 部分告警
* 有个弃用告警目录在 site-packages\scrapy_redis\dupefilter.py
### 遇到有的安装后无法导入,可能是历史残留影响
1. 卸载包
pip uninstall package
2. 清除缓存
C:\Users\*\AppData\Roaming\Python\Python311\site-packages\package
3. 重新安装
pip3 install package
## 部署scrapy
### 使用geray部署
#### 安装scapyd
* 使用pip3安装scrapyd，scrapyd的环境需要包含完整的requiremnets.txt依赖
```
pip3 install scrapyd
```
* 启动scrapyd
```
scrapyd
```
#### 安装gerapy
* 使用pip3安装gerapy
```
pip3 install gerapy
```
* 启动部署gerapy
```
gerapy init # 创建一个gerapy文件夹
gerapy migrate # 对数据库进行初始化
gerapy initadmin # 生成一个用户名和密码都是admin的管理员账号
gerapy createsuperuser # 如果不想创建admin的账号，运行该命令后，输入用户名和密码
gerapy runserver 0.0.0.0:8000 启动gerapy服务,访问http://host:8000
```

### 使用dcoker部署
### 使用k8s部署




