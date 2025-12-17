from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class Import_(Test):
    def setUp(self):
        super().setUp()

     
    def test_import(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Import")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-id_import-container"]'))
        ).click()
        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))
        )
        self.send_keys_and_wait(element, "Anagrafiche", wait_modal=False)
        self.wait_loader()

        file_path = os.path.join(os.getcwd(), 'test_import', 'example-anagrafiche.csv')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="file"]'))
        ).send_keys(file_path)

        self.wait_for_element_and_click('//button[@type="submit"]')
        self.wait_loader()

        ##TODO: finire test importazione