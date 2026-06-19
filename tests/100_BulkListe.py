from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test

class Liste(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.navigate_to_and_wait("Anagrafiche")

    def test_bulk_liste(self):
        #TODO: aggiorna liste
        self.aggiorna_liste()