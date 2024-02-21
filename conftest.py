import time
import pytest

from selenium.webdriver import Chrome, ChromeOptions

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.asset_page import AssetPage
from scripts.handle_logger import handle_logger


# 打开浏览器
# options = ChromeOptions()
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
browser = Chrome()


# 定义全局动作
@pytest.fixture(scope="session")
def driver():
    global browser

    browser.maximize_window()
    browser.implicitly_wait(30)

    yield

    browser.quit()


# 登录
@pytest.fixture(scope="module")
def init_login(driver):
    base_page = BasePage(browser)
    login_page = LoginPage(browser)
    asset_page = AssetPage(browser)
    handle_logger.info("\n{:=^40s}".format("开始执行登录功能测试用例"))

    yield base_page, login_page, asset_page

    handle_logger.info("\n{:=^40s}".format("登录功能测试用例执行结束"))


@pytest.fixture()
def refresh(driver):

    yield

    browser.refresh()
