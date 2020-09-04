from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = ""
    base_url = ""

    def __init__(self, reuse=False):
        # 如果发现浏览器是第一次调用

        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=opts)


        # 如果发现浏览器不是第一次调用
        else:
            self._driver = webdriver.Chrome()
            # 解决元素加载过慢的问题
            self._driver.implicitly_wait(3)

        if self.base_url != "":
            self._driver.get(self.base_url)
            self._driver.implicitly_wait(3)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for(self, fun):
        # 如果fun返回了True，那么就退出显示等待
        WebDriverWait(self._driver, 10).until(fun)
