import time

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.asset_locator import AssetLocator
from scripts.handle_config import handle_config
from scripts.handle_logger import handle_logger


class AssetPage(BasePage):
    """资产首页"""
    asset_locator = AssetLocator()

    def click_user_info(self):
        """点击用户个人中心"""
        self.get_user_info_element.click()

    @property
    def get_user_info_element(self) -> WebElement:
        """定位用户个人中心元素"""
        return self.wait_element_click(self.asset_locator.user_info_locator)

    @property
    def get_login_email_element(self) -> WebElement:
        """定位登录邮箱元素"""
        return self.wait_element_presence(self.asset_locator.login_email_locator)


if __name__ == '__main__':
    browser = Chrome()
    browser.maximize_window()
    browser.implicitly_wait(20)
    login_page = LoginPage(browser)
    asset_page = AssetPage(browser)
    time.sleep(2)
    login_page.login_input("lena.liu@spotec.net", "abc123")
    login_page.click_login()
    time.sleep(5)
    asset_page.click_user_info()
    time.sleep(2)
    print(asset_page.get_login_email_element.text)

