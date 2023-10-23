from tests.testbase import *


class ExampleLoginPage:
    def __init__(self, driver: WebDriver, locators: Locators):
        self.web = driver
        self.get = locators
        # todo: Elements:
        self.usernameInput = ('[data-test="username"]')
        self.passwordInput = ('[data-test="password"]')
        self.loginButton = ('[data-test="login-button"')

    def getLoginUserValue(self):
        return self.get.byID('login_credentials').text.split("\n")[1]

    def getLoginPasswordValue(self):
        return self.get.byClass('login_password').text.split("\n")[1]

    def enterUsername(self, username):
        self.get.bySelector(self.usernameInput).send_keys(username)

    def enterPassword(self, password):
        self.get.bySelector(self.passwordInput).send_keys(password)

    def submitLogin(self):
        self.get.bySelector(self.loginButton).click()


if __name__ == "__main__":
    pass
