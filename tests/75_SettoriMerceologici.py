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
        self.creazione_settori_merceologici("Settore Merceologico di Prova da Eliminare")

        # Modifica settore merceologico
        self.modifica_settori_merceologici("Settore Merceologico di Prova")
        
        # Cancellazione settore merceologico
        self.elimina_settore_merceologico()
        
        # Verifica settore merceologico
        self.verifica_settore_merceologico()

    def creazione_settori_merceologici(self, descrizione=str):
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        sleep(1)
        self.input(modal, 'Descrizione').setValue(descrizione)
        sleep(2)
        self.find(By.XPATH, '//button[@class="btn btn-primary"][@type="submit"]').click()

        self.wait_loader()

    def modifica_settori_merceologici(self, modifica=str):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_descrizione"]/input')
        element.send_keys('Settore Merceologico di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()

        sleep(2)          
        self.driver.execute_script('window.scrollTo(0,0)')

        self.input(None,'Descrizione').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Settori merceologici")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_settore_merceologico(self):
        self.navigateTo("Settori merceologici")
        self.wait_loader()    

        element=self.driver.find_element(By.XPATH,'//th[@id="th_descrizione"]/input')
        element.send_keys('Settore merceologico di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys(Keys.ENTER)

        sleep(1)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        
        sleep(2)          
        self.driver.execute_script('window.scrollTo(0,0)')

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_settore_merceologico(self):
        self.navigateTo("Settori merceologici")
        self.wait_loader()    

        #verifica elemento modificato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_descrizione"]/input')
        element.send_keys("Settore Merceologico di Prova")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Settore Merceologico di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_descrizione"]/input')
        element.send_keys("Settore Merceologico di Prova da Eliminare")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)