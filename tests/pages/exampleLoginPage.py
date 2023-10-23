from tests.testbase import *


class LoginPage:
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver
        self.get = locator
        self.usernameInput = lambda: self.get.byDataTest('username')
        self.passwordInput = lambda: self.get.byDataTest('password')
        self.submitButton = lambda: self.get.byDataTest('login-button')

    def enterUsername(self, inputValue: str):
        return self.usernameInput().send_keys(inputValue)

    def enterPassword(self, inputValue: str):
        return self.passwordInput().send_keys(inputValue)

    def submitLogin(self):
        return self.submitButton().click()
