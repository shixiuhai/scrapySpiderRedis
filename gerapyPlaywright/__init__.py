## 这里定义了一个打包的初始化,用于告诉gerapy这是一个包,用于成功部署到gerapy里
# # 暴露内部方法到本路径
from .downloadermiddlewares import PlaywrightMiddleware
from .request import PlaywrightRequest