from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CodaInvio(Test):
    def setUp(self):
        super().setUp()

        
    def test_coda_invio(self):
        self.navigateTo("Gestione email")
        self.navigateTo("Coda di invio")


