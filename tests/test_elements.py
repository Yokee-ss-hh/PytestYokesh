import logging
import time
from pages.elements import Elements
import pytest
from pages.landing_page import LandingPage


@pytest.mark.usefixtures("setup")
class TestElements:
    log_info = logging.getLogger()
    log_info.setLevel(logging.INFO)

    def test_verify_title(self):
        lp = LandingPage(self.driver)
        self.log_info.info("Navigated to website")
        self.log_info.info("Verifying landing page title")
        print(self.test_data["title"])
        assert lp.verify_landing_page() != self.test_data["title"]
        self.log_info.info("Landing page title is verified successfully")

    def test_verify_elements_page(self):
        ele = Elements(self.driver)
        self.log_info.info("Clicking on Elements button")
        self.log_info.info("Verifying elements page")
        print(self.test_data["title"])
        time.sleep(15)
        expected = self.test_data["title"]
        actual = ele.verify_elements_main_page()
        assert actual == expected
        self.log_info.info("Elements page title is verified successfully")




