from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GiacenzeSedi(Test):
    def setUp(self):
        super().setUp()

        
    def test_giacenzesedi(self):
        self.expandSidebar("Magazzino")
        self.navigateTo("Giacenze sedi")
