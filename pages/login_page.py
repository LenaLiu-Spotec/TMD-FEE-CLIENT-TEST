import time
import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from locators.login_locator import LoginLocators
from scripts.handle_config import handle_config
from scripts.handle_redis import handle_redis


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        url = handle_config("url", "client_login_url")
        self.login_locators = LoginLocators()
        self.driver.get(url)

    def input_accout(self, account):
        """输入登录账号"""
        self.click_and_input_element(self.get_account_input_element, account)

    def input_password(self, password):
        """输入登录密码"""
        self.click_and_input_element(self.get_password_input_element, password)

    def input_verify_code(self, verify_code):
        """输入登录验证码"""
        self.click_and_input_element(self.get_verify_code_input_element, verify_code)

    def click_login(self):
        """点击登录"""
        login_button_element = self.wait_element_click(self.login_locators.login_button_locator)
        login_button_element.click()

    def click_verify_code_login(self):
        """点击验证码登录"""
        verify_code_login_button_element = self.wait_element_click(self.login_locators.verify_code_button_locator)
        verify_code_login_button_element.click()

    def click_get_code(self):
        """点击获取验证码"""
        get_code_button_element = self.wait_element_click(self.login_locators.get_code_button_locator)
        get_code_button_element.click()

    @property
    def get_account_input_element(self) -> WebElement:
        """定位手机号/邮箱输入框"""
        return self.wait_element_presence(self.login_locators.account_input_locator)

    @property
    def get_password_input_element(self) -> WebElement:
        """定位密码输入框"""
        return self.wait_element_presence(self.login_locators.password_input_locator)

    @property
    def get_verify_code_input_element(self) -> WebElement:
        """定位验证码输入框"""
        return self.wait_element_presence(self.login_locators.verify_code_input_locator)

    @property
    def get_account_error_info_element(self) -> WebElement:
        """定位提示信息：账号错误、为空"""
        return self.wait_element_presence(self.login_locators.accout_info_locator)

    @property
    def get_password_error_info_element(self) -> WebElement:
        """定位提示信息：密码错误、为空"""
        return self.wait_element_presence(self.login_locators.password_info_locator)

    @property
    def get_verify_fail_info_element(self) -> WebElement:
        """定位验证失败提示信息：验证失败，请重试"""
        return self.wait_element_presence(self.login_locators.verify_fail_info_locator)

    @property
    def get_blcak_info_element(self) -> WebElement:
        """定位提示信息：账号拉黑"""
        return self.wait_element_presence(self.login_locators.black_info_locator)


if __name__ == '__main__':
    browser = Chrome()
    browser.maximize_window()
    browser.implicitly_wait(20)
    login_page = LoginPage(browser)
    login_page.click_verify_code_login()

    login_email = "lena-test105@1.com"
    login_page.input_accout(login_email)
    # login_page.input_password("abc123")

    login_page.click_get_code()
    time.sleep(2)

    code_type = handle_config("redis", "login_code_prefix")
    verify_code1 = handle_redis.get_code(code_type, login_email)
    login_page.input_verify_code(verify_code1)
    # login_page.input_verify_code("111111")
    login_page.click_login()
    time.sleep(1)

    # print(login_page.get_verify_fail_info_element.text)
    browser.quit()

