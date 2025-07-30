from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scadenzario(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")

    def test_creazione_scadenzario(self):
        # Crea una nuova scadenza. *Required*
        self.creazione_scadenzario("Cliente", "Scadenze generiche", "10", "Scadenza di Prova")
        self.creazione_scadenzario("Cliente", "Scadenze generiche", "10", "Scadenza di Prova da Eliminare")

        # Modifica scadenza
        self.modifica_scadenza("Scadenza di Prova")

        # Cancellazione scadenza
        self.elimina_scadenza()

        # Verifica scadenza
        self.verifica_scadenza()

        # Registrazione contabile (Azioni di gruppo)
        self.registrazione_contabile()

        # Info distinta (Azioni di gruppo)
        self.info_distinta()

    def creazione_scadenzario(self, nome: str, tipo: str, importo: str, descrizione: str):
                self.navigateTo("Scadenzario")
        self.wait_loader() 

        # Crea una nuova scadenza. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Tipo').setByText(tipo)
        self.input(modal, 'Anagrafica').setByText(nome)
        self.input(modal, 'Importo').setValue(importo)

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
    
    def modifica_scadenza(self, modifica:str):
                self.navigateTo("Scadenzario")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys('Scadenza di Prova', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        self.find(By.XPATH,'(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]').send_keys(modifica) 

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
                
        self.navigateTo("Scadenzario")
        self.wait_loader()  

    def elimina_scadenza(self):
                self.navigateTo("Scadenzario")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Descrizione-scadenza"]/i[@class="deleteicon fa fa-times"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys('Scadenza di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione-scadenza"]/i[@class="deleteicon fa fa-times"]').click()

    def verifica_scadenza(self):
                self.navigateTo("Scadenzario")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys("Scadenza di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Scadenza di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys("Scadenza da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click()
        
    def registrazione_contabile(self):
                self.navigateTo("Scadenzario")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys("Fattura immediata di acquisto numero 01", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        self.find(By.XPATH, '//a[@data-op="registrazione-contabile"]').click()

        # TODO: fare la registrazione contabile
        
        self.find(By.XPATH, '//button[@class="close"]').click()

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click()

    def info_distinta(self):
                self.navigateTo("Scadenzario")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input'))).send_keys("Fattura immediata di acquisto numero 01", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="change_distinta"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="distinta"]'))).send_keys("Prova") 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()

        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click()