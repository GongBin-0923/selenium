from test_appium.page.basepage import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.step("../page/search.yaml")
