from selenium.webdriver.common.by import By

from selenium3.page.add_member import AddMember
from selenium3.page.base_page import BasePage


class Index(BasePage):

    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#indexTop aside:nth-child(1) a:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "#_hmt_click div:nth-child(1) div:nth-child(4) div:nth-child(2) a:nth-child(1) div:nth-child(1) span:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_import_address(self):
        pass

    def goto_member_join(self):
        pass
