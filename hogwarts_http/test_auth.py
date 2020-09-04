import requests
from requests.auth import HTTPBasicAuth


def test_auth1():
    r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/gongbin/123",
                     auth=HTTPBasicAuth("gongbin", "123")
                     )
    print(r.text)
