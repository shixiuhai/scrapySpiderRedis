[切换到中文版](readme.md)
# Scaffold for Scrapy and Scrapy-Redis Based Spider
## Environment
### 1. Python 3.11.9
### 2. Scrapy 2.11.2
### 3. Scrapy-Redis 0.7.3 
### 4. Currently tested only on Windows, not yet tested on Linux
## Usage
### Create a new spider
### Configure Middleware (Middleware configurations can be previewed in middlewaresDemo)
#### Implemented Middleware
* Implemented IP proxy middleware: scrapyProxy.proxy.ProxyByHaiWaiMiddleware
## Other Notes
### Warnings
* There is a deprecation warning in site-packages\scrapy_redis\dupefilter.py
### Issue with Importing After Installation
1. Uninstall the package
2. Clear cache C:\Users*\AppData\Roaming\Python\Python311\site-packages\package
3. Reinstall pip3 install package
## deploy scrapy
### use geray deploy
#### intall scapyd
* install scrapyd using pip3, ensuring that the environment includes all dependencies listed in the requirements.txt file.
```
pip3 install scrapyd
```
* start scrapyd
```
scrapyd
```
#### install gerapy
* use pip3 安装gerapy
```
pip3 install gerapy
```
* start deploy gerapy
```
gerapy init # Create a gerapy folder
gerapy migrate # Initialize the database
gerapy initadmin # Generate a superuser with username and password as admin
gerapy createsuperuser # If you prefer not to use 'admin' as the username, run this command and provide a different username and password
gerapy runserver 0.0.0.0:8000 # Start Gerapy service, access at http://host:8000

```

### 使用dcoker部署
### 使用k8s部署









