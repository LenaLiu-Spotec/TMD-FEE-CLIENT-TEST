import os


# 当前项目根目录
BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
CONF_PATH = os.path.join(BATH_PATH, "confs")
CONF_FILE_PATH = os.path.join(CONF_PATH, "testcase.conf")

# 日志文件目录
LOG_PATH = os.path.join(BATH_PATH, "logs")

# 截图保存目录
IMG_PATH = os.path.join(BATH_PATH, "imgs")

# 报告文件目录
REPORT_PATH = os.path.join(BATH_PATH, "reports")
