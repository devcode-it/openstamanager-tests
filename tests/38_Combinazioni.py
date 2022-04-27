from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Combinazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_combinazioni(self, modifica="Combinazione di Prova"):
        self.creazione_combinazioni(codice="0001", nome="Combinazione di Prova da Modificare", categoria="Componenti", attributi="Attributo di Prova")
        self.creazione_combinazioni(codice="0002", nome="Combinazione di Prova da Eliminare", categoria="Componenti", attributi="Attributo di Prova")

        # Modifica Combinazioni
        self.navigateTo("Combinazioni")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Combinazione di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione Combinazioni
        self.navigateTo("Combinazioni")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Combinazione di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


    def creazione_combinazioni(self, codice: str, nome: str, categoria: str, attributi: str):
        self.navigateTo("Combinazioni")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Categoria')
        select.setByText(categoria)

        select = self.input(modal, 'Attributi')
        select.setByText(attributi)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       