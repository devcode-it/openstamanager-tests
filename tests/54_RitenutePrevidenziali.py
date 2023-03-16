from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RitenutePrevidenziali(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_ritenute_previdenziali(self):
        # Creazione ritenuta previdenziale      *Required*
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Modificare", percentuale="80,00", percentualeimp="60,00")
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Eliminare", percentuale="20,00", percentualeimp="40,00")

        # Modifica Ritenuta Previdenziale
        self.modifica_ritenute_previdenziali("Ritenuta Previdenziale di Prova")
        
        # Cancellazione Ritenuta Previdenziale
        self.elimina_ritenute_previdenziali()
              
        # Verifica Ritenuta Previdenziale
        self.verifica_ritenuta_previdenziale()

    def creazione_ritenute_previdenziali(self, descrizione=str, percentuale=str, percentualeimp=str):
        self.navigateTo("Ritenute previdenziali")
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Causale ritenuta').setValue("A")
        self.input(modal, 'Tipo ritenuta').setValue("RT01")
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_ritenute_previdenziali(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Previdenziale di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)  

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_ritenute_previdenziali(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Previdenziale di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)    

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()  
                
        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_ritenuta_previdenziale(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Previdenziale di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Ritenuta Previdenziale di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Previdenziale di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)