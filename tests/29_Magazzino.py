from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Magazzino(Test):
    def setUp(self):
        super().setUp()

        
    def test_magazzino(self):
        self.expandSidebar("Magazzino")

