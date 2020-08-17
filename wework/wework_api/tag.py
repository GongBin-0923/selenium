from jsonpath import jsonpath

from wework.wework_api.base_api import BaseApi
from wework.wework_api.wework import WeWork


class Tag(BaseApi):
    def __init__(self):
        secret = "SaP21rLwcdrYe0oJ2kYvXe7qN6-4FrdK9lVcIx_SmSU"
        self.token = WeWork().get_token(secret)

    def add(self, tagname, group_name):
        """
        创建标签
        :param tagname: 标签名
        :param group_name: 标签组
        :return:
        """
        add_data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": group_name,
                "tag": [{
                    "name": tagname
                }]
            }
        }
        # 先去查找需要创建的标签是否存在，利用jsonpath提取id值
        tag_id = jsonpath(self.get(""), f'$..tag[?(@.name=="{tagname}")].id')
        print(tag_id)

        if tag_id:
            # 若存在则先删除再创建
            print("已经存在此id，需要先删除再创建")
            self.delete(tag_id[0])
            ad_res = self.send_api(add_data)
            return ad_res
        else:

            return self.send_api(add_data)

    def get(self, get_id):
        get_data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag": [{
                    "id": get_id
                }]
            }
        }
        return self.send_api(get_data)

    def update(self, orig_name, update_name):
        id = jsonpath(self.get(""), f'$..tag[?(@.name=="{orig_name}")].id')
        updt_data = {
            "method": "pust",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": id,
                "name": update_name,
                "order": 1
            }
        }
        return self.send_api(updt_data)

    def delete(self, tag_id):
        delet_data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        print(self.send_api(delet_data))
        return self.send_api(delet_data)
