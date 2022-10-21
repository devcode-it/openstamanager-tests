from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Tabelle(Test):
    def setUp(self):
        super().setUp()

        
    def test_tabelle(self):
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")