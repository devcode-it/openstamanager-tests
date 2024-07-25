from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
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

    def modifica_banca(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Banche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Banca di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Banche")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_banca(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Banche")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Banca di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_banca(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Banche")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Banca di Prova", Keys.ENTER)
        sleep(1)
        
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Banca di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Banca di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

    def aggiorna_banca_fatture_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Banche") 
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_anagrafica-container"]').click() #seleziono Admin spa come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa")
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Banca Admin spa") #Banca Admin spa come nome della banca
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="iban"]'))).send_keys("IT11C1234512345678912345679") #seleziono IBAN
        sleep(2)
        
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input'))).send_keys("08", Keys.ENTER)    #cerco fattura numero 08
        self.wait_loader()
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-bank"]').click() #click su aggiorna banca
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click() #aggiorna banca in Admin spa
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        banca=self.find(By.XPATH, '(//tr[1]//td[9]//div)[2]').text  #controllo se è stata aggiornata la banca
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")
        sleep(2)

    def aggiorna_banca_scadenzario(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()  #vado in sezionale "Scadenzario clienti"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Scadenzario clienti")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_loader()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo-di-pagamento"]//input'))).send_keys("Bonifico", Keys.ENTER) #cerca il bonifico
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre azioni di gruppo
        sleep(1)

        self.find(By.XPATH, '//a[@data-op="change-bank"]').click() #apre aggiorna banca
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click() #aggiorna banca in Admin spa
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()
        sleep(1)

        widget=self.find(By.XPATH, '//div[@class="toast toast-success"]//div[3]').text  #se trova il widget il test è superato
        self.assertEqual(widget, "Banca aggiornata per le Fatture 0001/2024 !")  

        self.find(By.XPATH, '//tbody//tr//td').click() #tolgo checkbox
        self.find(By.XPATH, '//span[@class="select2-selection__clear"]').click() #esco dal sezionale
        self.wait_loader()

    def aggiorna_banca_fatture_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-bank"]').click()    #click su aggiorna banca
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_banca-container"]').click() #aggiorna banca in Admin spa
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Banca Admin spa")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()
        sleep(1)

        banca=self.find(By.XPATH, '(//tr[1]//td[7]//div)[2]').text  #controlla se la banca è stata aggiornata
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")
        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() #elimino fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

