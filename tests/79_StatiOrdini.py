from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StatiOrdini(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_stati_ordini(self):
        # Creazione stato contratti     *Required*
        self.creazione_stato_ordini("Stato degli Ordini di Prova da Modificare", "fa fa-check text-success", "#9d2929" )
        self.creazione_stato_ordini("Stato degli Ordini di Prova da Eliminare", "fa fa-thumbs-down text-danger", "#38468f")

        # Modifica Stato degli Ordini
        self.modifica_stato_ordini("Stato degli Ordini di Prova")
        
        # Cancellazione Stato degli Ordini
        self.elimina_stato_ordini()
           
        # Verifica Stato degli Ordini
        self.verifica_stato_ordini()

    def creazione_stato_ordini(self, descrizione=str, icona=str, colore=str):
        self.navigateTo("Stati degli ordini")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Icona').setValue(icona)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_stato_ordini(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Stati degli ordini")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Stato degli Ordini di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)  

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Stati degli ordini")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_stato_ordini(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Stati degli ordini")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Stato degli Ordini di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()     

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_stato_ordini(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Stati degli ordini")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Stato degli Ordini di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Stato degli Ordini di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Stato degli Ordini di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)