from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiPreventivi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_stati_preventivi(self):
        # Creazione stato preventivi    *Required*
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Modificare", "fa fa-check text-success")
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Eliminare", "fa fa-thumbs-down text-danger")

        # Modifica Stato dei preventivi
        self.modifica_stati_preventivi("Stato Preventivi di Prova")
        
        # Cancellazione Stato dei Preventivi
        self.elimina_stati_preventivi()
        
        # Verifica Stato dei Preventivi
        self.verifica_stati_preventivi()

    def creazione_stati_preventivi(self, descrizione = str, icona = str):
        self.navigateTo("Stati dei preventivi")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue("#000545")
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Icona').setValue(icona)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_stati_preventivi(self, modifica = str):
                self.navigateTo("Stati dei preventivi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Stato Preventivi di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')    

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Stati dei preventivi")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_stati_preventivi(self):
                self.navigateTo("Stati dei preventivi")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Stato Preventivi di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]') 

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()        

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_stati_preventivi(self):
                self.navigateTo("Stati dei preventivi")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Stato Preventivi di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Stato Preventivi di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Stato Preventivi di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)