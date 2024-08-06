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

    def test_impostazioni_anagrafiche(self):
        # Cambio formato codice anagrafiche (Anagrafiche)
        self.cambio_formato_codice()

    def cambio_formato_codice(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(2)
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        codice_element = self.find(By.XPATH, '//input[@id="codice"]')   #controllo se il codice ha formato 7 
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, "00000010")
        
        #elimino anagrafica
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti") 
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-1"]').click() #apro Anagrafiche
        sleep(1)

        formato=self.find(By.XPATH, '//input[@id="setting29"]') #cambio formato
        formato.clear()
        formato.send_keys("####", Keys.ENTER) #metto il formato a 4#
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(2)
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        codice_element = self.find(By.XPATH, '//input[@id="codice"]')   #controllo se il codice ha formato 4
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, "0010")  
        
        #elimino anagrafica
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-1"]').click() #apro Anagrafiche
        sleep(1)

        formato=self.find(By.XPATH, '//input[@id="setting29"]') #cambio formato
        formato.clear()
        formato.send_keys("#######", Keys.ENTER) #metto il formato a 7#
        sleep(2)

    