from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        # 如果发现浏览器是第一次调用
        self.driver = None
        if driver is None:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
            # 解决元素加载过慢的问题
            self.driver.implicitly_wait(3)

        # 如果发现浏览器不是第一次调用
        else:
            self.driver = driver
