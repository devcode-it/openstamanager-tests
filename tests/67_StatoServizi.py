from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class StatoServizi(Test):
    def setUp(self):
        super().setUp()

        
    def test_stato_servizi(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Stato dei servizi")
