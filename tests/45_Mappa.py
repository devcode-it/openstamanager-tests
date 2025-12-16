from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Mappa(Test):
    def setUp(self):
        super().setUp()

        
    def test_mappa(self):
        self.navigateTo("Mappa")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="mappa"]'))
        ).click()