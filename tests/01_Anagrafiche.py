from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html


class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Anagrafiche")

    def test_creazione_anagrafica(self, tipologia="Privato"):
        # Creazione anagrafiche *Required*
        self.add_anagrafica('Cliente', 'Cliente')  
        self.add_anagrafica('Tecnico', 'Tecnico') 
        self.add_anagrafica('Fornitore', 'Fornitore')
        self.add_anagrafica('Vettore', 'Vettore') 
        self.add_anagrafica('Agente', 'Agente')
        self.add_anagrafica('Anagrafica di Prova da Eliminare', 'Cliente')

        # Modifica anagrafica
        self.modifica_anagrafica()

        # Cancellazione anagrafica
        self.elimina_anagrafica()
      

    def add_anagrafica(self,nome=str, tipo=str):
        # Crea una nuova anagrafica del tipo indicato. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Denominazione').setValue(nome)

        select = self.input(modal, 'Tipo di anagrafica')
        select.setByText(tipo)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_anagrafica(self): 
        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Ragione-sociale"]/input')
        element.send_keys("Cliente")
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        sleep(1)
        select = self.find(By.XPATH, '//div[@id="module-edit"]//span[@class="selection"]//b[@role="presentation"]').click()
        self.wait_loader()

        select = self.find(By.XPATH, '//span[@class="select2-results"]//li[@class="select2-results__option"]').click()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

    def elimina_anagrafica(self):     
        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Ragione-sociale"]/input')
        element.send_keys('Anagrafica di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()