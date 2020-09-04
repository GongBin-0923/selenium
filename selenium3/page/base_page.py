from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver = ""

    def __init__(self, reuse=False):
        # 如果发现浏览器是第一次调用

        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)


        # 如果发现浏览器不是第一次调用
        else:
            self.driver = webdriver.Chrome()
            # 解决元素加载过慢的问题
            self.driver.implicitly_wait(3)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
