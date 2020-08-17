from wework.wework_api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "ww4d16179ba163502f"

    def get_token(self, SECRET):
        token_data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpid,
                "corpsecret": SECRET
            }
        }
        return self.send_api(token_data)['access_token']
