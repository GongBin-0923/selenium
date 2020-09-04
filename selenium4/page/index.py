from selenium.webdriver.common.by import By

from selenium4.page.add_member import AddMember
from selenium4.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.find(By.CSS_SELECTOR, "#indexTop aside:nth-child(1) a:nth-child(1)").click()
        self.find(By.CSS_SELECTOR,
                  "#_hmt_click div:nth-child(1) div:nth-child(4) div:nth-child(2) a:nth-child(1) div:nth-child(1) span:nth-child(1)").click()
        return AddMember(reuse=True)

    def goto_menu_contacts_and_add_member(self):
        def wait(driver):
            ele_len = len(self.finds(By.ID, "username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
                # 如果username存在就返回True
                # 如果不存在就返回Fals
            return ele_len >= 1

        self.wait_for(wait)

    def goto_member_join(self):
        pass
