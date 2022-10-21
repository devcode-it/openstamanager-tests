from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Campi_personalizzati(Test):
    def setUp(self):
        super().setUp()

        
    def test_acquisti(self):
        self.expandSidebar("Strumenti")
        self.expandSidebar("Stampe")

