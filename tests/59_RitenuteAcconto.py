from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RitenuteAcconto(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_ritenute_acconto(self):
        # Creazione ritenuta acconto        *Required*
        self.creazione_ritenute_acconto("Ritenuta Acconto di Prova da Modificare", "80,00", "60,00")
        self.creazione_ritenute_acconto("Ritenuta Acconto di Prova da Eliminare", "20,00", "40,00")
        
        # Modifica Ritenuta Acconto
        self.modifica_ritenuta_acconto("Ritenuta Acconto di Prova")
        
        # Cancellazione Ritenuta Acconto
        self.elimina_ritenuta_acconto()
         
        # Verifica Ritenuta Acconto
        self.verifica_ritenuta_acconto() 

    def creazione_ritenute_acconto(self, descrizione=str, percentuale=str, percentualeimp=str):
        self.navigateTo("Ritenute acconto")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
    
    def modifica_ritenuta_acconto(self, modifica):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute acconto")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Acconto di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)      

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ritenute acconto")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_ritenuta_acconto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute acconto")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Acconto di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()     

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_ritenuta_acconto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute acconto")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Acconto di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Ritenuta Acconto di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Acconto di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)