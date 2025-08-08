from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Aggiornamenti(Test):
    def setUp(self):
        super().setUp()

    def test_aggiornamenti(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Aggiornamenti")
        self.wait_loader()

        self.wait_for_element_and_click('//button[@onclick="checksum(this)"]')
        self.wait_for_element_and_click('//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal fade large-modal show"]')))

        self.wait_for_element_and_click('//button[@onclick="controlli(this)"]')
        self.wait_for_element_and_click('//button[@onclick="avviaControlli(this);"]')
        self.wait_for_element_and_click('//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal fade large-modal show"]')))

        self.wait_for_element_and_click('//button[@onclick="database(this)"]')
        self.wait_for_element_and_click('//button[@class="close"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal fade large-modal show"]')))

