from selenium4.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index(reuse=True)

    def test_add_member(self):
        # goto_add_member实例化了 AddMember
        add_member = self.index.goto_add_member()
        add_member.add_member()
        assert "abcde" in add_member.get_first()
