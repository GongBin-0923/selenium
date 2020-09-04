from selenium.webdriver.common.by import By

from selenium3.page.base_page import BasePage


class AddMember(BasePage):
    # 在添加页面输入内容保存
    def add_member(self):
        self.driver.find(By.ID, "username").send_keys("abcde")
        self.driver.find(By.ID, "memberAdd_acctid").send_keys("abcdsddde")
        self.driver.find(By.ID, "memberAdd_phone").send_keys("18655552222")
        # 保存
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        # 获取成员列表第一个元素
        return self.driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(1) td:nth-child(2)").get_attribute(
            "title")
