from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TipiScadenze(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
       
    def test_creazione_tipiscadenze(self, modifica="Tipo di Scadenza di Prova"):
        self.creazione_tipiscadenze(nome= "Tipo di Scadenza di Prova da Modificare",descrizione= "Descrizione tipo di Scadenza")
        self.creazione_tipiscadenze(nome= "Tipo di Scadenza di Prova da Eliminare",descrizione= "Descrizione tipo di Scadenza")

        # Modifica Tipo di scadenza
        self.navigateTo("Tipi scadenze")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Tipo di Scadenza di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione Tipo di scadenza
        self.navigateTo("Tipi scadenze")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Tipo di Scadenza di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()        


    def creazione_tipiscadenze(self, nome=str, descrizione=str):
        self.navigateTo("Tipi scadenze")

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

