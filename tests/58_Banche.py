from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Banche(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_banca(self):
        # Creazione banca       *Required*
        self.creazione_banca("Cliente", "Banca di Prova da Modificare", "IT11C1234512345678912345679", "12345678")
        self.creazione_banca("Cliente", "Banca di Prova da Eliminare", "IT11C1234512345678912345679", "12345678")

        # Modifica Banca
        self.modifica_banca("Banca di Prova")
        
        # Cancellazione Banca
        self.elimina_banca()
        
        # Verifica Banca
        self.verifica_banca()

        # Aggiorna Banca (Azioni di gruppo) da Fatture di acquisto
        self.aggiorna_banca_fatture_acquisto()

        # Aggiorna Banca (Azioni di gruppo) da Scadenzario
        self.aggiorna_banca_scadenzario()

        # Aggiorna Banca (Azioni di gruppo) da Fatture di Vendita
        self.aggiorna_banca_fatture_vendita()

    def creazione_banca(self, anagrafica: str, nome: str, iban: str, bic: str):
        self.navigateTo("Banche")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Anagrafica')
        select.setByText(anagrafica)
        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'IBAN').setValue(iban)
        self.input(modal, 'BIC').setValue(bic)
        
        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_banca(self, modifica = str):
                self.navigateTo("Banche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Banca di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Banche")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_banca(self):
                self.navigateTo("Banche")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Banca di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_banca(self):
                self.navigateTo("Banche")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Banca di Prova", Keys.ENTER)
        
        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Banca di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Banca di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

    def aggiorna_banca_fatture_acquisto(self):
                self.navigateTo("Banche") 
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_anagrafica-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Banca Admin spa") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="iban"]'))).send_keys("IT11C1234512345678912345679")
        
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input'))).send_keys("3", Keys.ENTER) 
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="change-bank"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        banca = self.find(By.XPATH, '//tbody//tr//td[9]').text 
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")

    def aggiorna_banca_scadenzario(self):
                self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Scadenzario clienti")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_loader()

        # TODO: allineare ai documenti presenti, nessuna scadenza ha metodo di pagamento Bonifico
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo-di-pagamento"]//input'))).send_keys("Bonifico", Keys.ENTER) #cerca il bonifico

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()

        self.find(By.XPATH, '//a[@data-op="change-bank"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        widget = self.find(By.XPATH, '//div[@class="toast toast-success"]//div[3]').text 
        self.assertEqual(widget, "Banca aggiornata per le Fatture 0001/2025 !")  

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//span[@class="select2-selection__clear"]').click() 
        self.wait_loader()

    def aggiorna_banca_fatture_vendita(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="change-bank"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        banca = self.find(By.XPATH, '//tbody//tr//td[7]').text  
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")
        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

