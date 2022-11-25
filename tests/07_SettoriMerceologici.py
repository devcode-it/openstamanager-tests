from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SettoriMerceologici(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Anagrafiche")
        self.navigateTo("Settori merceologici")

    def test_creazione_settori_merceologici(self):
        # Creazione settore merceologico      *Required*
        self.creazione_settori_merceologici("Settore Merceologico di Prova da Modificare")

        # Modifica settore merceologico
        self.modifica_settori_merceologici("Settore Merceologico di Prova")

        self.creazione_settori_merceologici("Settore Merceologico di Prova da Eliminare")
        # Cancellazione settore merceologico
        self.elimina_settore_merceologico()
        
        # Verifica settore merceologico
        self.verifica_settore_merceologico()

    def creazione_settori_merceologici(self, descrizione=str):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus'))).click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"][@type="submit"]'))).click()
        self.wait_loader()

    def modifica_settori_merceologici(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys('Settore Merceologico di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Settori merceologici")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

    def elimina_settore_merceologico(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Settori merceologici")
        self.wait_loader()    
        

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys('Settore merceologico di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]'))).click()
        sleep(1)    

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_settore_merceologico(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Settori merceologici")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys("Settore Merceologico di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Settore Merceologico di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys("Settore Merceologico di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)