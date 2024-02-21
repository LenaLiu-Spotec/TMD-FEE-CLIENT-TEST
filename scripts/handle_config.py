from configparser import ConfigParser

from scripts.constants import CONF_FILE_PATH


class HandleConfig(ConfigParser):
    """处理配置文件"""
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __call__(self, section="DEFAULT", option=None, is_eval=False, is_bool=False):
        """
        读取配置文件，并处理读取结果
        :param section: 配置文件区域名
        :param option: 配置文件选项名，可为空
        :param is_eval: 是否将读取结果进行eval()转换
        :param is_bool: 是否将读取结果进行getboolean()转换
        :return:
        """
        # 1、读配置文件
        self.read(self.filename, encoding="utf-8")

        # 2、如果选项名为空，则读取整个区域结果，并将结果存入字典
        if option is None:
            return dict(self[section])

        # 3、如果is_bool为bool类型且为true，则进行getboolean()转换
        if isinstance(is_bool, bool):
            if is_bool:
                return self.getboolean(section=section, option=option)
        else:
            raise ValueError("is_bool必须为bool类型")

        # 4、option不为空且is_bool为false时，读取配置文件
        data = self.get(section=section, option=option)

        # 5、如果读取的结果全为数字，则进行int、float转换
        if data.isdigit():
            return int(data)
        else:
            try:
                return float(data)
            except Exception as e:
                pass

        # 6、如果is_eval为bool类型且为ture，则进行eval()转换
        if isinstance(is_eval, bool):
            if is_eval:
                return eval(data)
        else:
            raise ValueError("is_eval必须为bool类型")

        return data


handle_config = HandleConfig(CONF_FILE_PATH)

if __name__ == '__main__':
    handle_config1 = HandleConfig(CONF_FILE_PATH)
    print(handle_config1("test"))
    print(handle_config1("test", "c"))
    print(handle_config1("test", "a", is_bool=True))
    print(handle_config1("test", "b", is_eval=True))
    print(type(handle_config1("wait", "timeout")))
    print(type(handle_config1("wait", "poll_frequency")))

