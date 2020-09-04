from test_appium.page.basepage import BasePage
from test_appium.page.search import Search


class Market(BasePage):
    def go_to_search(self):
        self.step("../page/market.yaml")
        return Search(self._driver)
