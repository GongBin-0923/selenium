import base64
import json

import requests


def test_encode():
    url = "http://127.0.0.1:9999/demo.txt"
    r = base64.b64decode(requests.get(url).content)
    res = json.loads(r)

    print(res)


class TestApi():
    # 优化后代码
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_encode1(self, data: dict):
        r = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(r.content))
        elif data["encoding"] == "qita":
            return
