from tests.testbase import *


class LoginPage:
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver
        self.get = locator
        self.usernameInput = lambda: self.get.byDataTest('username')
        self.passwordInput = lambda: self.get.byDataTest('password')
        self.submitButton = lambda: self.get.bySelector('[type="submit"]')

    def login(self, username, password):
        self.usernameInput().send_keys(username)
        self.passwordInput().send_keys(password)

    def clickButtonSubmit(self):
        self.submitButton().click()
