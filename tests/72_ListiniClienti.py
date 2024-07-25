from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Listini(Test):
    def setUp(self):
        super().setUp()
        self.navigateTo("Magazzino")


    def test_creazione_listino_cliente(self):
        # Crea un nuovo listino cliente. *Required*
        self.creazione_listino_cliente("Listino cliente di Prova da Modificare","01/12/2024", "01/01/2024")
        self.creazione_listino_cliente("Listino cliente di Prova da Eliminare", "01/12/2024", "01/01/2024")
        
        # Modifica listino cliente
        self.modifica_listino_cliente("Listino cliente di Prova")
        
        # Cancellazione listino cliente
        self.elimina_listino_cliente()
        
        # Verifica listino cliente
        self.verifica_listino_cliente()

        # Aggiorna listino cliente (Azione di gruppo) da anagrafiche
        self.aggiorna_listino_cliente()

        # Aggiungi a listino cliente (Azioni di gruppo) da Articoli
        self.aggiungi_a_listino_cliente()

    def creazione_listino_cliente(self, nome:str, dataatt: str, datascad: str):
        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Data attivazione').setValue(dataatt)
        self.input(modal, 'Data scadenza default').setValue(datascad)
        self.input(modal, 'Nome').setValue(nome)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_listino_cliente(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Listini cliente")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Listino cliente di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--single"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("001", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="btn-group btn-group-flex"]//button[@class="btn btn-primary"]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("10,00")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]'))).send_keys("10")
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-success"])[2]'))).click()
        sleep(1)

        self.input(None,'Nome').setValue(modifica)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="back"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_listino_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Listini cliente")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Listino cliente di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_listino_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Listini cliente")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Listino cliente di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Listino cliente di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Listino cliente di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

    def aggiorna_listino_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)   #cerca Cliente
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziona cliente
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="aggiorna-listino"]'))).click()    #click su aggiorna listino
        self.find(By.XPATH, '//span[@id="select2-id_listino-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Listino cliente di Prova", Keys.ENTER)   #seleziona "Listino cliente di Prova"
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click()  #apre anagrafica "Cliente" 
        self.wait_loader()

        self.find(By.XPATH, '(//span[@class="select2-selection__clear"])[4]').click()   #toglie listino
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva 
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/i[@class="deleteicon fa fa-times"]').click()    #cancella ricerca
        sleep(1)

    def aggiungi_a_listino_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="add-listino"]').click() #click su aggiungi a listino cliente
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_listino-container"]').click() #scelgo il listino "Listino cliente di Prova"
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]'))).send_keys("10")   #seleziono 10% di sconto
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click su procedi
        self.wait_loader()

        self.navigateTo("Listini cliente")
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() #click sul listino
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tr[1]//td[8]'))) #controlla se l'articolo è stato aggiunto al listino
        self.find(By.XPATH, '//tr[1]//td[9]//a[2]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()  #tolgo l'articolo dal listino
        self.wait_loader()
        