from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html


class Newsletter(Test):
    def setUp(self):
        super().setUp()

        
    def test_creazione_newsletter(self):
        self.expandSidebar("Gestione email")
        
        # Crea una nuova newsletter. *Required*   
        self.add_newsletter('Newsletter di Prova da Modificare', "Contratto")
        self.add_newsletter('Newsletter di Prova da Eliminare', "Ddt")

        # Modifica newsletter
        self.modifica_newsletter("Newsletter di Prova")
     
        # Cancellazione newsletter
        self.elimina_newsletter()

        # Verifica newsletter
        self.verifica_newsletter()

        
    def add_newsletter(self, nome: str, modulo: str):
    
        self.navigateTo("Newsletter")

        # Crea una nuova newsletter
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        select = self.input(modal, 'Template email')
        select.setByText(modulo)
    
        self.input(modal, 'Nome').setValue(nome)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_newsletter(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Newsletter")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Newsletter di Prova da Modificare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Newsletter")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_newsletter(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Newsletter")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Newsletter di Prova da Eliminare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_newsletter(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Newsletter")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Newsletter di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Newsletter di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Newsletter di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)