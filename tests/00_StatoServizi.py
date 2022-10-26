from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html

class StatoServizi(Test):
    def setUp(self):
        super().setUp()

        
    def test_stato_servizi(self):

        #Attivazione moduli nascosti
        self.attiva_moduli()

        #Aggiunta P.IVA e dati anagrafica azienda   
        self.compila_azienda()

        #Aggiunta Google API Key
        self.api_key()



    def attiva_moduli(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Stato dei servizi")
        self.find(By.XPATH, '//button[@class="btn btn-success btn-xs"]//i[@class="fa fa-recycle"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-success btn-xs"]//i[@class="fa fa-recycle"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-success btn-xs"]//i[@class="fa fa-recycle"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-success btn-xs"]//i[@class="fa fa-recycle"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.find(By.XPATH, '//button[@class="btn btn-success btn-xs"]//i[@class="fa fa-recycle"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()


    def compila_azienda(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_nazione-container"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Italia")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        
        self.input(None, 'Partita IVA').setValue("05024030289")
        self.input(None, 'Codice fiscale').setValue("05024030289")
        element=self.driver.find_element(By.XPATH,'//input[@id="indirizzo"]')
        element.send_keys("Via Rovigo, 51")
        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")

        self.find(By.XPATH, '//a[@id="save"]').click()


    def api_key(self):
        self.navigateTo("Strumenti")
        self.navigateTo("Impostazioni")

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ricerca_impostazioni"]'))).send_keys("Google Maps API key", Keys.ENTER)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-2"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting61"]'))).send_keys("AIzaSyC0vGSW3zSzCCEhMzO5JVhkeJR7HmuDelg", Keys.ENTER)

