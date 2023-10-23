import pytest
from tests.testbase import *


class TestSuiteLogin:

    # *ExampleTest: uses a fixture "Login" as precondition, then validate that inventory list page has 6 items
    def test_login_success(self, loginSuccessful: tuple[WebDriver, Locators]):
        web, get = loginSuccessful

        items = get.byClasses('inventory_item')
        expect(len(items)).toBeEqual(6)


if __name__ == "__main__":
    pytest.main()
