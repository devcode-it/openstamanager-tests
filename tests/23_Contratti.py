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


class Contratti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")


    def test_creazione_contratto(self):
        # Crea una nuovo contratto *Required*
        importi = RowManager.list()
        self.creazione_contratto("Contratto di Prova da Modificare", "Cliente", "1", importi[0])

        # Duplica un contratto *Required*
        self.duplica_contratto()

        # Modifica Contratto
        self.modifica_contratto("Contratto di Prova")

        # Cancellazione contratto
        self.elimina_contratto()     

        # Verifica contratto
        self.verifica_contratto()

    def creazione_contratto(self, nome:str, cliente: str, stato: str, file_importi: str):
        self.navigateTo("Contratti")
        self.wait_loader() 

        # Crea una nuovo contratto per il cliente indicato. 
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        self.input(modal, 'Stato').setByIndex(stato)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        row_manager.compile(file_importi)

    def duplica_contratto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//td[@class="bound clickable"]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="pulsanti-modulo"]//button[@class="btn btn-primary ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))).click()
        self.wait_loader()

        element=self.find(By.XPATH,'//input[@id="nome"]')
        element.clear()
        element.send_keys("Contratto di Prova da Eliminare") 
        self.find(By.XPATH, '//a[@id="save"]').click()
        self.wait_loader()

    def modifica_contratto(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Contratti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('=Contratto di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        element=self.find(By.XPATH,'//input[@id="nome"]')
        element.clear()
        element.send_keys(modifica) 
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_contratto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Contratti")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Contratto di Prova da Eliminare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_contratto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Contratti")
        self.wait_loader()  

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Contratto di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Contratto di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Contratto di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)