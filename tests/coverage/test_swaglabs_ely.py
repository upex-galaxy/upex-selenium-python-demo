import pytest
from tests.testbase import *


class TestSuiteLogin:

    # *TC1
    def test_login_success(self, beforeEach: Test):
        web, get = beforeEach

        get.byDataTest('username').send_keys('standard_user')
        get.byDataTest('password').send_keys('secret_sauce')
        get.byDataTest('login-button').click()


if __name__ == "__main__":
    pytest.main()
