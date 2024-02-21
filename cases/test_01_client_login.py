import time
import pytest

from datas import login_datas
from scripts.handle_logger import handle_logger


class TestLogin:
    """测试交易端登录功能"""
    @pytest.mark.error
    @pytest.mark.parametrize("account_error_data", login_datas.login_account_error)
    def test_account_error(self, account_error_data, init_login, refresh):
        """测试登录账号错误"""
        base_page, login_page, asset_page = init_login
        login_page.input_accout(account_error_data["account"])
        login_page.input_password(account_error_data["password"])
        login_page.click_login()
        time.sleep(0.5)
        actual_ele = login_page.get_account_error_info_element

        try:
            assert account_error_data["msg"] == actual_ele.text, "测试登录时账号错误或为空时失败"
        except AssertionError as e:
            handle_logger.error("具体异常为: {}".format(e))
            raise e

    @pytest.mark.error
    @pytest.mark.parametrize("password_error_data", login_datas.login_password_error)
    def test_password_error(self, password_error_data, init_login, refresh):
        """测试登录密码错误"""
        base_page, login_page, asset_page = init_login
        login_page.input_accout(password_error_data["account"])
        login_page.input_password(password_error_data["password"])
        login_page.click_login()
        time.sleep(0.5)
        actual_ele = login_page.get_password_error_info_element

        try:
            assert password_error_data["msg"] == actual_ele.text, "测试登录时密码错误或为空时失败"
        except AssertionError as e:
            handle_logger.error("具体异常为：{}".format(e))
            raise e

    # @pytest.mark.error
    # @pytest.mark.parametrize("code_error_data", login_code_error)
    # def test_code_error(self, code_error_data, init_login):
    #     """测试登录密码错误"""
    #     base_page, login_page, asset_page = init_login
    #     login_page.login_input(code_error_data["account"], code_error_data["code"])
    #     login_page.click_login()
    #     time.sleep(0.5)
    #     actual_ele = login_page.get_password_error_info_element
    #
    #     try:
    #         assert code_error_data["msg"] == actual_ele.text, "测试登录时密码错误或为空时失败"
    #     except AssertionError as e:
    #         handle_logger.error("具体异常为：{}".format(e))
    #         raise e

    @pytest.mark.invalid
    @pytest.mark.parametrize("invalid_data", login_datas.login_invalid)
    def test_account_invalid(self, invalid_data, init_login, refresh):
        """测试黑名单账号"""
        base_page, login_page, asset_page = init_login
        login_page.input_accout(invalid_data["account"])
        login_page.input_password(invalid_data["password"])
        login_page.click_login()
        time.sleep(0.7)
        actual_ele = login_page.get_blcak_info_element

        try:
            assert invalid_data["msg"] == actual_ele.text, "测试登录时黑名单账号时失败"
        except AssertionError as e:
            handle_logger.error("具体异常为：{}".format(e))
            raise e

    @pytest.mark.success
    @pytest.mark.parametrize("success_data", login_datas.login_success)
    def test_login_success(self, success_data, init_login, refresh):
        """测试登录成功"""
        base_page, login_page, asset_page = init_login
        login_page.input_accout(success_data["account"])
        login_page.input_password(success_data["password"])
        login_page.click_login()
        asset_page.click_user_info()
        time.sleep(0.5)
        actual_ele = asset_page.get_login_email_element

        try:
            assert success_data["msg"] == actual_ele.text, "测试登录失败"
        except AssertionError as e:
            handle_logger.error("具体异常为：{}".format(e))
            raise e


if __name__ == '__main__':
    # pytest.main(["-m", "invalid"])
    pytest.main()
