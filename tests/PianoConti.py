from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PianoConti(Test):
    def setUp(self):
        super().setUp()

       
    def test_pianoconti(self):
        self.navigateTo("Contabilità")
        self.navigateTo("Piano dei conti")
