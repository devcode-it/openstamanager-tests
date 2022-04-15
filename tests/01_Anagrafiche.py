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

        # Crea una nuova anagrafica di tipo Cliente.
        self.add_anagrafica('Cliente', 'Cliente', '05024030289')

        # Crea una nuova anagrafica di tipo Tecnico.   
        self.add_anagrafica('Tecnico', 'Tecnico', '12345678910')

        # Crea una nuova anagrafica di tipo Fornitore.   
        self.add_anagrafica('Fornitore', 'Fornitore', '10987654321')

        # Crea una nuova anagrafica di tipo Vettore.   
        self.add_anagrafica('Vettore', 'Vettore', '1231231231')

        # Crea una nuova anagrafica di tipo Agente.   
        self.add_anagrafica('Agente', 'Agente', '3123213211')

        # Crea una nuova anagrafica da cancellare.
        self.add_anagrafica('Anagrafica di prova da cancellare', 'Cliente', '05024030289')

        # Modifica anagrafica

        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Ragione-sociale"]/input')
        element.send_keys('Cliente')
        
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


        # Cancellazione anagrafica

        self.navigateTo("Anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Ragione-sociale"]/input')
        element.send_keys('Anagrafica di prova da cancellare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


    def add_anagrafica(self, name = 'ANAGRAFICA DI PROVA', tipo = 'Cliente', partita_iva = ''):
        # Crea una nuova anagrafica del tipo indicato. '''
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Denominazione').setValue(name)

        modal.find_element(By.CSS_SELECTOR, '.btn-box-tool').click()
        self.input(modal, 'Partita IVA').setValue(partita_iva)

        select = self.input(modal, 'Tipo di anagrafica')
        select.setByText(tipo)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

