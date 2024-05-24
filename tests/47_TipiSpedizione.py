from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TipiSpedizione(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        
    def test_creazione_tipi_spedizione(self):
        # Creazione tipo di spedizione *Required*
        self.creazione_tipi_spedizione("Tipo di Spedizione di Prova da Modificare")
        self.creazione_tipi_spedizione("Tipo di Spedizione di Prova da Eliminare")

        # Modifica Tipo di spedizione
        self.modifica_tipi_spedizione("Tipo di Spedizione di Prova")
        
        # Cancellazione Tipo di spedizione
        self.elimina_tipi_spedizione()
        
        # Verifica Tipo di spedizione
        self.verifica_tipi_spedizione()

    def creazione_tipi_spedizione(self, descrizione=str):
        self.navigateTo("Tipi di spedizione")

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_tipi_spedizione(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di spedizione")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di Spedizione di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)    

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()
        
        self.navigateTo("Tipi di spedizione")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_tipi_spedizione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di spedizione")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di Spedizione di Prova da Eliminare', Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1) 

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click() 

    def verifica_tipi_spedizione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi di spedizione")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di Spedizione di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Tipo di Spedizione di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di Spedizione di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)