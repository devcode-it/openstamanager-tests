from common.Test import Test, get_html
from selenium.webdriver.common.by import By

class Listini(Test):
    def setUp(self):
        super().setUp()

        
    def test_listini(self):
        self.expandSidebar("Magazzino")
        self.navigateTo("Listini")
        ##TODO: test listini
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')