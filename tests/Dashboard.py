from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Dashboard(Test):
    def setUp(self):
        super().setUp()

      
    def test_Dashboard(self):
        self.navigateTo("Dashboard")
