from test_appium.page.app import App


class TestSearch():
    def test_1search(self):
        App().start().zhuye().go_to_market().go_to_search().search("jd")
