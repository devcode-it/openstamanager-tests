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
       
    def test_creazione_tipi_scadenze(self):
        # Creazione tipo di scadenza    *Required*
        self.creazione_tipi_scadenze(nome= "Tipo di Scadenza di Prova da Modificare",descrizione= "Descrizione tipo di Scadenza da Modificare")
        self.creazione_tipi_scadenze(nome= "Tipo di Scadenza di Prova da Eliminare",descrizione= "Descrizione tipo di Scadenza da Eliminare")

        # Modifica Tipo di scadenza
        self.modifica_tipi_scadenze("Tipo di Scadenza di Prova")
        
        # Cancellazione Tipo di scadenza
        self.elimina_tipi_scadenze()

        # Verifica Tipo di scadenza
        self.verifica_tipi_scadenze()
        
    def creazione_tipi_scadenze(self, nome=str, descrizione=str):
        self.navigateTo("Tipi scadenze")

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Descrizione').setValue(descrizione)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_tipi_scadenze(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi scadenze")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Tipo di Scadenza di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()      
        sleep(1)  

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Tipi scadenze")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_tipi_scadenze(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi scadenze")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Tipo di Scadenza di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()        

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_tipi_scadenze(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Tipi scadenze")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Tipo di Scadenza di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Tipo di Scadenza di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Tipo di Scadenza di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)