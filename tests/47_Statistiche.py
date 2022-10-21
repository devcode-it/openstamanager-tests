from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GiacenzeSedi(Test):
    def setUp(self):
        super().setUp()

        
    def test_giacenze_sedi(self):
        self.navigateTo("Statistiche")
