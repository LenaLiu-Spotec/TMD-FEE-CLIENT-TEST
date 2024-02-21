import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from scripts.handle_config import handle_config
from scripts.handle_logger import handle_logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = handle_config("wait", "timeout")
        self.poll_frequency = handle_config("wait", "poll_frequency")

    def wait_element_click(self, locator):
        """
        等待元素可点击
        :param locator:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
            return wait.until(expected_conditions.element_to_be_clickable(locator))
        except(TimeoutException, NoSuchElementException) as e:
            handle_logger.error("等待元素超时或找不到元素")
            raise e

    def wait_element_presence(self, locator):
        """
        等待元素出现
        :param locator:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
            return wait.until(expected_conditions.presence_of_element_located(locator))
        except(TimeoutException, NoSuchElementException) as e:
            handle_logger.error("等待元素超时或找不到元素")
            raise e

    def wait_element_visibility(self, locator):
        """
        等待元素可见
        :param locator:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
            return wait.until(expected_conditions.visibility_of_element_located(locator))
        except(TimeoutException, NoSuchElementException) as e:
            handle_logger.error("等待元素超时或找不到元素")
            raise e

    def click_element(self, locator):
        """单击鼠标"""
        try:
            ActionChains(self.driver).click(locator).perform()
        except(TimeoutException, NoSuchElementException) as e:
            handle_logger.error("等待元素超时或找不到元素")
            raise e

    def click_and_input_element(self, locator, info):
        """单击输入框并输入参数"""
        try:
            ActionChains(self.driver).click(locator).send_keys(info).perform()
        except(TimeoutException, NoSuchElementException) as e:
            handle_logger.error("等待元素超时或找不到元素")
            raise e


if __name__ == '__main__':
    browser = Chrome()
    browser.maximize_window()
    browser.implicitly_wait(20)
    base_page = BasePage(browser)
    browser.get("http://192.168.0.129:8030/zh-CN/sign/login")
    time.sleep(1)
    # account_element = browser.find_element(By.ID, "account")
    # ActionChains(browser).click(account_element).send_keys("lena.liu@spotec.net").perform()
    # password_element = browser.find_element(By.ID, "password")
    # ActionChains(browser).click(password_element).send_keys("abc123").perform()
    account_locator = (By.ID, "account")
    account_element = base_page.wait_element_presence(account_locator)
    base_page.click_and_input_element(account_element, "lena.liu@spotec.net")
    password_locator = (By.ID, "password")
    password_element = base_page.wait_element_presence(password_locator)
    base_page.click_and_input_element(password_element, "abc123")
    browser.find_element(By.CLASS_NAME, "login-button").click()
    time.sleep(2)
