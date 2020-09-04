from appium import webdriver

from test_appium.page.basepage import BasePage
from test_appium.page.zhuye import Zhuye


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = 'com.xueqiu.android.common.MainActivity'

    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['noReset'] = 'true'
            # # "noReset":True 不重置相关环境
            # disired_caps['dontStopAppOnReset'] = 'true'
            # #"dontStopAppOnReset":True 表示在首次启动时不停止app
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            # 当需要输入中文时需要添加的两个选项
            self._driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(60)
        else:
            self._driver.start_activity(self._package, self._activity)

        return self

    def zhuye(self):
        return Zhuye(self._driver)
