from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnitaMisura(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Unità di misura")

    def test_creazione_unitamisura(self, modifica="UdMdP"):
        self.creazione_unitamisura(valore= "UdMdPdM")
        self.creazione_unitamisura(valore= "UdMdPdE")

        # Modifica Unità di Misura
        self.navigateTo("Unità di misura")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys('UdMdPdM')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        
        self.input(None,'Valore').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione Unità di Misura
        self.navigateTo("Unità di misura")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Valore"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Valore"]/input')
        element.send_keys('UdMdPdE')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Valore"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()      


    def creazione_unitamisura(self, valore= str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Valore').setValue(valore)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()