import datetime
import redis

from scripts.handle_config import handle_config


class HandleRedis:
    """读取redis数据库"""

    # 1、链接redis库
    def __init__(self):
        self.res_conn = redis.Redis(host=handle_config("redis", "host"),
                                    port=handle_config("redis", "port"),
                                    password=None,
                                    db=handle_config("redis", "db"),
                                    encoding="utf-8",
                                    decode_responses=True)

    # 2、获取数据
    def get_value(self, res_data):
        return self.res_conn.get(res_data)

    # 3、获取验证码
    def get_code(self, code_type, account):
        today_str = str(datetime.datetime.now().date())
        res_data = code_type + account + today_str
        return eval(self.res_conn.get(res_data))


handle_redis = HandleRedis()

if __name__ == '__main__':
    handle_redis1 = HandleRedis()
    code_type1 = handle_config("redis", "login_code_prefix")
    print(handle_redis1.get_code(code_type1, "lena-test105@1.com"))


