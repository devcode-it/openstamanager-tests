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


class Preventivi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")

    def test_creazione_preventivo(self, modifica = "Preventivo di Prova"):
        # Crea un nuovo preventivo
        importi = RowManager.list()
        self.creazione_preventivo("Preventivo di Prova da Modificare","Cliente", "1", importi[0])
        self.creazione_preventivo("Preventivo di Prova da Eliminare","Cliente", "1", importi[0])

        # Modifica preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione preventivo
        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def creazione_preventivo(self, nome:str, cliente:str, idtipo: str, file_importi: str):
        self.navigateTo("Preventivi")
        self.wait_loader() 

        # Crea un nuovo preventivo per il cliente indicato. 
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome preventivo').setValue(nome)
        
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        select = self.input(modal, 'Tipo di Attività')
        select.setByIndex(idtipo)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto preventivo', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)
