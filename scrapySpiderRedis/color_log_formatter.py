import logging
import coloredlogs
from scrapy.logformatter import LogFormatter

class ColorLogFormatter(LogFormatter):
    def format(self, record):
        coloredlogs.install(level='DEBUG', fmt='%(levelname)s: %(message)s', logger=logging.getLogger())
        return super().format(record)
