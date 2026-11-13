from common.Test import Test, get_html
from selenium.webdriver.common.by import By

class Listini(Test):
    def setUp(self):
        super().setUp()

        
    def test_listini(self):
        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Listini")
        ##TODO: test listini
