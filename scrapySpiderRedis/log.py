import datetime
import logging
import logging.handlers
import os
import colorlog
from scrapySpiderRedis.settings import LOG_LEVEL, SAVE_LOGS
class Logging:
    def __init__(self, log_file_name, log_file_path="./logs"):
        """
        :param log_file_path:
                                    1、print(os.getcwd()) # 获取当前工作目录路径
                                    2、print(os.path.abspath('.')) # 获取当前工作目录路径
        :param log_file_name:
                                    1、current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
                                    2、weight_path = os.path.join(current_work_dir, weight_path)  # 再加上它的相对路径，这样可以动态生成绝对路径
        """
        self.log_colors_config = {
            'DEBUG': 'cyan',  # cyan white
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
        # log文件存储路径
        self.log_file_path = log_file_path
        self.log_file_name = log_file_name
        self.save_to_file = SAVE_LOGS

        if self.save_to_file:
            self._log_filename = self.get_log_filename()

        # 创建一个日志对象
        self._logger = logging.getLogger(self.log_file_name)

        # 设置控制台日志的输出级别: 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
        self.set_console_logger()
        if self.save_to_file:
            self.set_file_logger()
        self._logger.setLevel(LOG_LEVEL)

    def get_log_filename(self):
        if not os.path.isdir(self.log_file_path):
            # 创建文件夹
            os.makedirs(self.log_file_path)
        return f"{self.log_file_path}/{self.log_file_name}_{str(datetime.date.today())}.log"

    def set_console_logger(self):
        formatter = colorlog.ColoredFormatter(
            # fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            fmt='%(log_color)s[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=self.log_colors_config)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

    def set_file_logger(self):
        # 日志文件信息输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s -> %(funcName)s - line:%(lineno)d - %(levelname)s: %(message)s')
        # 将输出日志信息保存到文件中
        file_handler = logging.handlers.RotatingFileHandler(
            self._log_filename, maxBytes=10485760, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

    def get_logger(self):
        return self._logger


if __name__ == '__main__':
    logger = Logging("scrapy.log").get_logger()
    logger.debug('test log')
