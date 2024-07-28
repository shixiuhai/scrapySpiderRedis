import pymysql
from scrapySpiderRedis.items import *
from scrapySpiderRedis.settings import MYSQL_HOST, MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_USER
import importlib

# 获取MySQL连接信息
host = MYSQL_HOST
user = MYSQL_USER
password = MYSQL_PASSWORD
database = MYSQL_DATABASE
port = MYSQL_PORT

def create_or_update_mysql_table(class_name_str):
    # 导入包含 Item 类的模块
    module_name = 'scrapySpiderRedis.items'
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
        return
    
    # 获取 Item 类
    try:
        item_class = getattr(module, class_name_str)
    except AttributeError:
        print(f"Error: Class '{class_name_str}' not found in module '{module_name}'.")
        return
    
    # 连接MySQL数据库
    connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
    cursor = connection.cursor()

    # 获取 Item 类的字段列表
    fields = [field for field in item_class.fields.keys() if field != 'table']
    
    # 获取当前表结构
    cursor.execute(f"SHOW TABLES LIKE '{item_class.table}'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        # 获取当前表的字段信息
        cursor.execute(f"DESCRIBE {item_class.table}")
        existing_columns = cursor.fetchall()
        existing_fields = {column[0] for column in existing_columns}

        # 找出需要添加的字段
        fields_to_add = set(fields) - existing_fields
        for field in fields_to_add:
            alter_table_sql = f"ALTER TABLE {item_class.table} ADD COLUMN {field} VARCHAR(1000)"
            cursor.execute(alter_table_sql)

        # 找出需要删除的字段
        fields_to_remove = existing_fields - set(fields)
        for field in fields_to_remove:
            alter_table_sql = f"ALTER TABLE {item_class.table} DROP COLUMN {field}"
            cursor.execute(alter_table_sql)
    else:
        # 构建 CREATE TABLE 语句
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {item_class.table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            {', '.join([f'{field} VARCHAR(1000)' for field in fields])}
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cursor.execute(create_table_sql)

    # 提交并关闭连接
    connection.commit()
    connection.close()

# 获取用户输入的类名
class_name_input = input("请输入要创建或更新表的类名（该类名应存在于 scrapySpiderRedis.items 模块中，例如 'LvItem'）：").strip()

# 调用创建或更新表函数
create_or_update_mysql_table(class_name_input)
