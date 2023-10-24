from tests.testbase import *


class FooterPage:
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver
        self.get = locator
        self.allLinksOnFooter = lambda link: self.get.bySelector(
            f'[class="footer"] [class="social"] [class="social_{link}"] a')

    def clickLink(self, targetLink):
        self.allLinksOnFooter(targetLink).click()
