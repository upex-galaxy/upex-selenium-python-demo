import pytest
from tests.testbase import *


class TestSuite:
    # * Este es otro ejemplo de Suite usando otro Fixture y con más de un caso de Prueba:

    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get
        web = setWebDriver
        get = Locators(web)

        get.page("https://www.selenium.dev/selenium/web/web-form.html")
        title = web.title
        assert title == "Web form"

        yield
        web.quit()

    def test_TC1_FirstExample(self, precondition):

        textBox = get.bySelector("[name='my-text']")
        submitButton = get.bySelector("[type='submit']")
        textBox.send_keys("Selenium")
        submitButton.click()
        message = get.byID("message")
        value = message.text
        assert value == "Received!"

    def test_TC2_SecondExample(self, precondition):

        textBox = get.bySelector("[name='my-text']")
        submitButton = get.bySelector("[type='submit']")
        textBox.send_keys("UPEX")
        submitButton.click()
        message = get.byID("message")
        value = message.text
        assert value == "Received!"


if __name__ == '__main__':
    pytest.main()
