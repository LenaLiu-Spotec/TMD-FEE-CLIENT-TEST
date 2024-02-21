from selenium.webdriver.common.by import By


class AssetLocator:
    """资产页元素定位表达式"""

    # 用户个人中心元素定位表达式
    user_info_locator = (By.CLASS_NAME, "tmd-dropdown-trigger")

    # 登录邮箱元素定位表达式
    login_email_locator = (By.XPATH, "//div[@class='tpeyeECh']/div[@class='XBPqWO4Q']")
