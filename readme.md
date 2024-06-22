# scrapy-redis脚手架
## 环境
### 1. python3.11.9
### 2. scrapy2.11.2
### 3. scrapy-redis0.7.3 
### 4. 暂时只做了在windows环境下运行,尚未测试linux下
## 使用
### 新建一个爬虫
```
scrapy genspider cwcwclothingSpider cwcwclothing.com
```
### 配置中间件(需要配置的中间件在middlewaresDemo可以预览)
#### 实现的中间件
* 完成了IP代理中间件scrapyProxy.proxy.ProxyByHaiWaiMiddleware
## 其他
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
* 使用gerapy安装gerapy
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




