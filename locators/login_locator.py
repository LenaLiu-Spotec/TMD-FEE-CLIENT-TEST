from selenium.webdriver.common.by import By


class LoginLocators:
    """登录页面元素定位表达式"""

    # 手机/邮箱输入框元素定位表达式
    account_input_locator = (By.ID, "account")

    # 密码输入框元素定位表达式
    password_input_locator = (By.ID, "password")

    # 验证码登录按钮元素定位表达式
    verify_code_button_locator = (By.XPATH, "//span[@class='color-link']")

    # 获取验证码按钮元素定位表达式
    get_code_button_locator = (By.CLASS_NAME, "countdown-text")

    # 验证码输入框元素定位表达式
    # verify_code_input_locator = (By.CLASS_NAME, "label-input-affix")
    verify_code_input_locator = (By.ID, "code")

    # 登录按钮元素定位表达式
    login_button_locator = (By.CLASS_NAME, "login-button")

    # 账号为空、错误时提示信息元素定位表达式
    accout_info_locator = (By.ID, "account_help")

    # 密码为空、错误时提示信息元素定位表达式
    password_info_locator = (By.ID, "password_help")

    # 验证失败时提示信息元素定位表达式
    verify_fail_info_locator = (By.CLASS_NAME, "tmd-form-item-explain-error")

    # 黑名单客户提示信息元素定位表达式
    black_info_locator = (By.CLASS_NAME, "tmd-notification-notice-description")

    # 注册按钮元素定位表达式
    register_button_locator = (By.XPATH, "//a[@class='color-link']")
