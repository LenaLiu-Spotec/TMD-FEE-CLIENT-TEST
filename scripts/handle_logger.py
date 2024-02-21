import os
import logging

from concurrent_log_handler import ConcurrentRotatingFileHandler

from scripts.constants import LOG_PATH
from scripts.handle_config import handle_config


class HandleLogger:
    """处理日志"""
    def __init__(self):
        self.case_logger = logging.getLogger(handle_config("log", "log_name"))
        self.case_logger.setLevel(handle_config("log", "log_level"))

        # 定义终端日志
        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(handle_config("log", "console_level"))
        # simple_formatter = logging.Formatter(handle_config("log", "simple_formatter"))
        # console_handler.setFormatter(simple_formatter)
        # self.case_logger.addHandler(console_handler)

        # 1、定义日志文件名称、内存
        file_handler = ConcurrentRotatingFileHandler(filename=os.path.join(LOG_PATH, handle_config("log", "file_name")),
                                                     maxBytes=handle_config("log", "maxBytes"),
                                                     backupCount=handle_config("log", "backupCount"),
                                                     encoding="utf-8")

        # 2、日志文件设置日志等级
        file_handler.setLevel(handle_config("log", "file_level"))

        # 3、设置日志文件内容
        verbose_formatter = logging.Formatter(handle_config("log", "verbose_formatter"))
        file_handler.setFormatter(verbose_formatter)

        # 4、添加日志文件到日志器
        self.case_logger.addHandler(file_handler)

    def get_logger(self):
        """返回日志器"""
        return self.case_logger


handle_logger = HandleLogger().get_logger()

if __name__ == '__main__':
    handle_logger = HandleLogger().get_logger()
    handle_logger.info("这是info日志")
    handle_logger.error("这是error日志")
