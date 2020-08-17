from wework.wework_api.base_api import BaseApi
from wework.wework_api.tag import Tag


class TestTag(BaseApi):
    def test_add_tag(self):
        add_res = Tag().add("hao123", "tudou1")
        print(add_res)

    def test_get_tag(self):
        get_res1 = Tag().get("eti7IFCgAA_HvNNmzCD4-eQO8hUZALrg")
        print(get_res1)

    def test_update_tag(self):
        update_res = Tag().update("hao123", "jahskdh")
        print(update_res)

    def test_delete_tag(self):
        delete_res = Tag().delete("eti7IFCgAA_HvNNmzCD4-eQO8hUZALrg")
        print(delete_res)
