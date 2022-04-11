from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Aggiornamenti(Test):
    def setUp(self):
        super().setUp()

        
    def test_aggiornamenti(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Aggiornamenti")
