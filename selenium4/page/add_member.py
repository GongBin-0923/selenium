from selenium.webdriver.common.by import By

from selenium4.page.base_page import BasePage


class AddMember(BasePage):
    # 在添加页面输入内容保存
    def add_member(self):
        self.driver.find(By.ID, "username").send_keys("abcde")
        self.driver.find(By.ID, "memberAdd_acctid").send_keys("abcdsddde")
        self.driver.find(By.ID, "memberAdd_phone").send_keys("18655552222")
        # 保存
        self.driver.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        # 找出符合要求的所有element
        elements = self.finds(By.CSS_SELECTOR, "#member_list td:nth-child(2)")
        teamer = []
        # 对所有element进行遍历，依次取出其中的title属性并存入数组
        for element in elements:
            teamer.append(element.get_attribute("title"))
        return teamer
