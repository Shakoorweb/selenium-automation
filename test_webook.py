import pytest

from webook_automation import WebookAutomation


class TestWebook:

    @pytest.fixture()
    def setup(self):
        webook = WebookAutomation()
        yield webook

    def test_registration(self, setup):
        webook = setup
        assert webook.registration_flow("First Name", "Last name", "demo321@gmail.com", "admin1234",
                                        "549192675")

    def test_search(self, setup):
        webook = setup
        assert webook.search("Messi")

    def test_filter(self, setup):
        webook = setup
        assert webook.filter_search("Events")
