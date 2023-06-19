from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Import_(Test):
    def setUp(self):
        super().setUp()

     
    def test_import(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Import")

        self.find(By.XPATH, '//*[@id="select2-id_import-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Anagrafiche", Keys.ENTER)
        self.wait_loader()

        self.find(By.XPATH, '//input[@id="file"]').send_keys(os.path.join(os.getcwd(), 'example-anagrafiche.csv'))
        sleep(1)

        self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()