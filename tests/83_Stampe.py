from common.Test import Test, get_html
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
        self.navigate_to_and_wait("Stampe")
        
        self.click_first_table_row()
        ##TODO: finire test stampa