from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

    def creazione_ritenute_previdenziali(self, descrizione = str, percentuale = str, percentualeimp = str):
        self.navigateTo("Ritenute previdenziali")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Causale ritenuta').setValue("A")
        self.input(modal, 'Tipo ritenuta').setValue("RT01")
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_ritenute_previdenziali(self, modifica = str):
                self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Previdenziale di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')  

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_ritenute_previdenziali(self):
                self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Ritenuta Previdenziale di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')    

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()  
                
        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_ritenuta_previdenziale(self):
                self.navigateTo("Ritenute previdenziali")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Previdenziale di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Ritenuta Previdenziale di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Ritenuta Previdenziale di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)