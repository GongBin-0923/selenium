from test_appium.page.basepage import BasePage
from test_appium.page.market import Market


class Zhuye(BasePage):
    def go_to_market(self):
        self.step("../page/zhuye.yaml")
        return Market(self._driver)
