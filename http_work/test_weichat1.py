import requests


class TestWeWork():
    def setup(self):
        # 获取token
        ID = "ww4d16179ba163502f"
        SECRET = "_drrVKC8-NzLjeb3IxvkBfxG9_SNF4z2J82v9dHNmMo"
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}")
        self.token = res.json()['access_token']

    def test_edit_department(self):
        # 先去查询部门
        department_name = "potato"
        id = 3
        department_instans = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id={id}")

        # 创建部门的数据
        department_information = {
            "name": department_name,
            "parentid": 1
        }
        # 判断部门是否已经存在若存在则先删除再创建，若不存在则直接创建
        if department_instans.json()["errcode"] == 0:
            de_res = requests.get(
                f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}")
            print(de_res.json())
            cre_res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
                                    json=department_information)
            print(cre_res.json())
        else:
            cre_res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
                                    json=department_information)
            print(cre_res.json())

        # 修改部门
        modify_data = {
            "id": id,
            "name": "tudousanhao"
        }
        mdf_res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
                                json=modify_data)
        print(mdf_res.json())

        # 删除部门
        dele_res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}")
        print(dele_res.json())

        # 获取所有部门查看部门是否还存在
        re = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id= ")
        print(re.json())
