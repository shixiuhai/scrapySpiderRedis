[Switch to English Version](readmeEnglish.md)
# 基于scrapy和scrapy-redis爬虫的脚手架
## 环境
### 1. python3.11.9
### 2. scrapy2.11.2
### 3. scrapy-redis0.7.3 
### 4. windows和linux测试都做了
### 5. 欢迎大家提交修改和建议
## 使用
### 备注
* 项目默认清理了所有不必要配置，如果要运行demo请参考spidersDemo，将内部文件替换到scrapySpiderRedis内
* 不同配置文件的切换通过settings里的env参数配置，默认是dev环境，dev环境的配置在settings_dev.py里，prod环境的配置在settings_prod.py里
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
* 可以将并发请求设置为 CONCURRENT_REQUESTS=1
* yield 迭代的使用一般是 Request 回调函数里，
yield func ，func里面一般return就行，func里面可以返回多个item，在外边循环 yiled item就行

### 配置中间件(需要配置的中间件在middlewaresDemo可以预览)
#### 实现的中间件
* 完成了IP代理中间件scrapyProxy.ProxyByHaiWaiMiddleware(IP代理)
* 完成了下载中间件gerapyPlaywright.PlaywrightMiddleware(playwright动态渲染)
* 完成了下载中间件gerapySelenium.SeleniumMiddleware(selenium by chrome渲染)
## 其他
### 项目内的中文翻译成英文
* 英文文档不是最新
* 暂时做不动了,谁有兴趣请联系邮箱15256728901@163.com或issue
### 部分告警
* 有个弃用告警目录在 site-packages\scrapy_redis\dupefilter.py
* 在使用selenium渲染的时候记得把settings.py里CONCURRENT_REQUESTS=2设置小些,CONCURRENT_REQUESTS表示请求并非数量
* yield 的函数里面一般是retrun
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




