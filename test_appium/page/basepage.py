import yaml
from Scripts._testmultiphase import Str
from appium.webdriver.webdriver import WebDriver
from typing import List, Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _black_list = [(By.XPATH, "//*[@text='等待']")]
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locate):
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                              locate)
            _error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count > self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locate)
            raise e

    def send(self, sendkey, locate, by):
        try:
            send_keys = self.find(by, locate)
            return send_keys.send_keys(sendkey)
        except Exception as e:
            self._error_count += 1
            if self._error_count > self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(sendkey, locate, by)
            raise e

    def step(self, path, ):
        with open(path, encoding="utf-8") as f:
            steps: List[Dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if step["action"] == "click":
                        return element.click()
                    if step["action"] == "send":
                        content: Str = step["value"]
                        for param in self._params.values():
                            content = content.replace("%s" % param, self._params['param'])
                        return element.send_keys(content)
