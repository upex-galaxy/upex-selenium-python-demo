from tests.testbase import *


class FooterPage:
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver
        self.get = locator
        self.allLinksOnFooter = lambda link: self.get.bySelector(
            f'[class="footer"] [class="social"] [class="social_{link}"] a')

    def clickLink(self, targetLink):
        self.allLinksOnFooter(targetLink).click()

    def switchNewTab(self, defaultTab):
        AllTabs = self.web.window_handles
        for windowHand in AllTabs:
            if windowHand != defaultTab:
                self.web.switch_to.window(windowHand)
                break

    def getHrefAttrib(self, targetLink):
        hrefAttrib = self.allLinksOnFooter(targetLink).get_attribute('href')
        return hrefAttrib
