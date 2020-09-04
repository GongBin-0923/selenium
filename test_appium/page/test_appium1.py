from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXQ():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # # "noReset":True 不重置相关环境
        # disired_caps['dontStopAppOnReset'] = 'true'
        # #"dontStopAppOnReset":True 表示在首次启动时不停止app
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 当需要输入中文时需要添加的两个选项

        desired_caps['automationName'] = 'uiautomator2'
        # 安卓默认工作引擎

        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_serch(self):
        self.driver.find_element_by_id("asd").click()
        element = self.driver.find_element_by_xpath("//*[@resourceid='asdas' and @text='阿里巴巴']")
        element.is_enabled()
        element.get_attribute()

    def test_touchaction(self):
        # 利用touchaction实现点击、滑动等操作
        # touchaction的操作都要加perform才能执行
        action = TouchAction(self.driver)
        action.press(x=731, y=2083).move_to(x=731, y=484).release().perform()

        # 滑动解锁
        action = TouchAction(self.driver)
        action.press(x=243, y=395).wait(100).move_to(x=721, y=378).wait(100).move_to(x=1190, y=364).release().perform()

    def test_location(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        current_price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        print(current_price)
        assert float(current_price) > 200

    def test_uiautomator(self):
        # 利用安卓原生uiautomator定位
        self.driver.find_element_by_android_uiautomator("new UiSelector().text('0988')")

        # 也可以是组合定位，例如id与text属性、class与text的属性
        id_text = 'new Uiselector().resourceId("resource-id的值").text("text的值")'
        self.driver.find_element_by_android_uiautomator(id_text).click()
        class_text = 'new Uiselector().className("class的值").text("text的值")'
        self.driver.find_element_by_android_uiautomator(class_text).click()

        # 父子关系定位
        son = 'new Uiselector().resourceId("resource-id的值").childSelector(text("text的值"))'
        self.driver.find_element_by_android_uiautomator(son).click()

        # 兄弟关系定位
        brother = 'new Uiselector().resourceId("resource-id的值").fromParent(text("text的值"))'
        self.driver.find_element_by_android_uiautomator(brother).click()

    def scroll_find_element(self):
        # 滚动查找
        scroll_selector = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("text的值").instance(0));'
        self.driver.find_element_by_android_uiautomator(scroll_selector).click()
        pass

    def test_webdriverwait(self):
        # 显示等待
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        locate = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locate))
        # 或者WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locate))
        current_price = self.driver.find_element(*locate).text
        print(current_price)
        cur_p = float(current_price)
        assert cur_p > 200

    def test_toast(self):
        # 定位toast控件
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "make a Popup").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']")
        # print(self.driver.page_source)
        # 打印页面元素（dom）
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contain(@text,'clicked popup')]").text)
        # 定位toast

    def test_hamcrest(self):
        # hamrest断言
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        locate = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locate))
        # 或者WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locate))
        current_price = self.driver.find_element(*locate).text
        print(current_price)
        expect_price = 260
        cur_p = float(current_price)
        # 接近某个值
        assert_that(cur_p, close_to(expect_price, expect_price * 0.1))

        isinstance()
