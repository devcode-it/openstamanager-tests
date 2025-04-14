from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

    def test_impostazioni_anagrafiche(self):
        # Test impostazione Formato codice anagrafica
        self.cambio_formato_codice()

        ## TODO: test geolocalizzazione automatica

    def cambio_formato_codice(self):
        wait = WebDriverWait(self.driver, 20)

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        codice_element = self.find(By.XPATH, '//input[@id="codice"]')
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, "00000010")
        
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti") 
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Anagrafiche"]').click()
        sleep(1)

        formato = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Formato codice anagrafica")]//input')
        formato.clear()
        formato.send_keys("####", Keys.ENTER) 

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        codice_element = self.find(By.XPATH, '//input[@id="codice"]') 
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, "0010")
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Anagrafiche"]').click()
        sleep(1)

        formato = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Formato codice anagrafica")]//input')
        formato.clear()
        formato.send_keys("########", Keys.ENTER)
        sleep(1)

    