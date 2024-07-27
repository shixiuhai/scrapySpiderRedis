"""
初始化mysql数据库表
"""
import pymysql
from scrapySpiderRedis.items import *
from scrapySpiderRedis.settings import MYSQL_HOST,MYSQL_DATABASE,MYSQL_PASSWORD,MYSQL_PORT,MYSQL_USER
import importlib
# 创建MySQL表的函数
def create_mysql_table(class_name_str):
    # 导入包含 LvItem 的模块
    module_name = 'scrapySpiderRedis.items'
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
        return
    
    # 获取 LvItem 类
    try:
        item_class = getattr(module, class_name_str)
    except AttributeError:
        print(f"Error: Class '{class_name_str}' not found in module '{module_name}'.")
        return
    
    # 从Scrapy配置中获取MySQL连接信息
    host = MYSQL_HOST
    user = MYSQL_USER
    password = MYSQL_PASSWORD
    database = MYSQL_DATABASE

    # 连接MySQL数据库
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()

    # 获取LvItem类的字段列表
    fields = [field for field in item_class.fields.keys() if field != 'table']

    # 构建CREATE TABLE语句
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {item_class.table} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        {', '.join([f'{field} VARCHAR(1000)' for field in fields])}
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """

    # 执行SQL语句
    cursor.execute(create_table_sql)

    # 提交并关闭连接
    connection.commit()
    connection.close()

# 获取用户输入的类名
class_name_input = input("请输入要创建表的类名（例如 LvItem）：").strip()

# 调用创建表函数
create_mysql_table(class_name_input)