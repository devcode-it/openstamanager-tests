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



class Scadenzario(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")


    def test_creazione_scadenzario(self, modifica = "Scadenza di Prova"):
        # Crea una nuova scadenza. 
        self.creazione_scadenzario("Scadenze generiche", "10", "Scadenza di Prova da Modificare")
        self.creazione_scadenzario("Scadenze generiche", "10", "Scadenza di Prova da Eliminare")


        # Modifica scadenza
        self.navigateTo("Scadenzario")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione-scadenza"]/input')
        element.send_keys('Scadenza di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Descrizione').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione scadenza
        self.navigateTo("Scadenzario")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Descrizione-scadenza"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione-scadenza"]/input')
        element.send_keys('Scadenza di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


    def creazione_scadenzario(self, tipo: str, importo: str, descrizione: str):
        self.navigateTo("Scadenzario")
        self.wait_loader() 

        # Crea una nuova scadenza. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Tipo').setByText(tipo)
        self.input(modal, 'Importo').setValue(importo)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunta scadenza', toast)
    
        
        