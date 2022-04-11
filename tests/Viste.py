from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Viste(Test):
    def setUp(self):
        super().setUp()

      
    def test_viste(self):
        self.navigateTo("Strumenti")
        self.navigateTo("Viste")
