from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppiumWeWork1():
    package = '"com.tencent.wework'
    activity = '.launch.WwMainActivity'

    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = self.package
        desired_caps['appActivity'] = self.activity
        desired_caps['noReset'] = 'true'
        # # "noReset":True 不重置相关环境
        # disired_caps['dontStopAppOnReset'] = 'true'
        # #"dontStopAppOnReset":True 表示在首次启动时不停止app
        desired_caps['autoGrantPermissions'] = 'true'
        # 自动点击一些权限通过的按钮
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 当需要输入中文时需要添加的两个选项
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def back(self):
        yield
        self.driver.back()

    @pytest.mark.parametrize("membername, gender, phonenumber", [
        ('测试name1', '女', '18622222221'),
        ('测试name2', '男', '18622222222'),
        ('测试name3', '女', '18622222223'),
        ('测试name4', '男', '18622222224'),
        ('测试name5', '女', '18622222225'),
        ('测试name6', '男', '18622222226'),
        ('测试name7', '女', '18622222227'),
        ('测试name8', '男', '18622222228'),
        ('测试name9', '女', '18622222229'),
        ('测试name14', '男', '18622222230'),
        ('测试name15', '女', '18622222231'),
        ('测试name16', '男', '18622222232'),
        ('测试name17', '女', '18622222233'),
        ('测试name10', '男', '18622222234'),
        ('测试name11', '女', '18622222235'),
        ('测试name12', '男', '18622222236'),
        ('测试name13', '女', '18622222237'
                          ''),
    ])
    def test_add_member(self, membername, gender, phonenumber, back):
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='通讯录' ]")
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/eas' and @text='通讯录' ]")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        el3.click()
        # 滚动查找

        scroll_selector = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, scroll_selector).click()
        # 点击手动添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/cl5").click()
        # 填入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/bat']/*[@text='必填']").send_keys(
            f"{membername}")
        # 点击性别
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/efz").click()
        # 选择性别
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/eas' and @text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/eas' and @text='女']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fh_").send_keys(f"{phonenumber}")

        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        sleep(1)
        # 判断是否添加成功
        assert "添加成功" in self.driver.page_source
        print("添加成功")

    def test_delete_member(self):
        # 点击通讯录
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eas' and @text='通讯录' ]")
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/eas' and @text='通讯录' ]")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        el3.click()
        # 选取所有包含“测试name”的元素
        ui_locator = 'new UiSelector().textContains("测试name")'
        elememts = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, ui_locator)
        # 当存在的元素大于0时候进行删除
        if len(elememts) > 0:
            for element in elememts:
                # 点击联系人
                element.click()
                # 点击右上角功能按钮
                de_locator = (MobileBy.ID, "com.tencent.wework:id/hvd")
                WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(de_locator))
                self.driver.find_element(*de_locator).click()
                # 点击编辑成员
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b87").click()
                # 点击删除成员
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/efq").click()
                # 删除确认
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bit").click()
                return self.test_delete_member()
