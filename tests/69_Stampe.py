from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class Stampe(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")

    def test_stampe(self):
        self.stampe()

    def stampe(self):
                self.navigateTo("Stampe")
        self.wait_loader()
        
        self.wait_for_element_and_click('//tbody//tr//td[2]')