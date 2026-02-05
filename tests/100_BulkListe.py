from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test

class Liste(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.navigateTo("Anagrafiche")

    def test_bulk_liste(self):
        #TODO: aggiorna liste
        self.aggiorna_liste()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')