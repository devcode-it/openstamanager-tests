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


class TecniciTariffe(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Attività")
        self.navigateTo("Tecnici e tariffe")
        self.wait_loader()

    def test_tecnicitariffe(self, modifica = "28.00"):

        # Modifica Tariffe
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Tecnico')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@class="input-group has-feedback"]/input[@id="costo_ore1"]').send_keys(modifica)
    
                
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()
