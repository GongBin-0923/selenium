from hamcrest import *
import requests
from jsonpath import jsonpath


class TestDemo():
    def test_hogwarts_json(self):
        # json断言
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        # jsonpath只接受json object
        assert jsonpath(r.json(), '$..name')[0] == '社区治理'

    def test_hamcrest(self):
        # 使用复杂断言规则的时候使用
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('社区治理'))

    def test_transfer_cookie(self):
        # 通过header传递
        url = "https://httpbin.testing-studio.com/cookies"
        header = {"cookis": "hogwarts=school",
                  "User-Agent": "gongbin"
                  }
        # r=requests.get(url=url,headers=header)
        # print(r.request.headers)

        # 通过cookies参数进行传递
        cookie_data = {"hogwarts": "schools",
                       "teacher": "AD"
                       }
        r = requests.get(url=url, cookies=cookie_data)
        print(r.request.headers)
