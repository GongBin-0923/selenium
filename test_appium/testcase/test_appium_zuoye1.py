from time import sleep

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppiumWeWork():
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
        self._driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(10)

    def teardown_class(self):
        self._driver.quit()

    @pytest.mark.parametrize('connectman', ['土豆一号', '雷达二'])
    def test_appium_wework(self, connectman):
        el3 = self._driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/eas' and @text='通讯录' ]")
        el3.click()
        el4 = self._driver.find_element_by_id("com.tencent.wework:id/hvn")
        el4.click()

        el7 = self._driver.find_element_by_id("com.tencent.wework:id/gfs")
        el7.send_keys(connectman)
        element_locator = (By.XPATH, f"//*[@class='android.widget.TextView' and @text='{connectman}']")
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
        el8 = self._driver.find_element_by_xpath(f"//*[@class='android.widget.TextView' and @text='{connectman}']")
        el8.click()
        el9 = self._driver.find_element_by_id("com.tencent.wework:id/ai9")
        el9.click()
        el10 = self._driver.find_element_by_id("com.tencent.wework:id/ei_")
        el10.send_keys("测试code")
        el11 = self._driver.find_element_by_id("com.tencent.wework:id/ei6")
        el11.click()
        self._driver.back()
