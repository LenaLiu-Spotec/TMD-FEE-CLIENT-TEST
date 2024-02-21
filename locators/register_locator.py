from selenium.webdriver.common import by


class RegisterLocator:
    """注册页面元素表达式"""
    # 确认密码输入框元素定位表达式
    comfirm_password_input_locator = (By.ID, "confirmPassword")
