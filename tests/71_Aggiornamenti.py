from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test, get_html

class Aggiornamenti(Test):
    def setUp(self):
        super().setUp()

        
    def test_aggiornamenti(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Aggiornamenti")
        self.wait_loader()    

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="checksum(this)"]'))).click()
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="database(this)"]'))).click()
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="controlli(this)"]'))).click()
        self.find(By.XPATH, '//button[@onclick="avviaControlli(this);"]').click()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))).click()