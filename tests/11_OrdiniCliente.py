from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OrdiniCliente(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")


    def test_creazione_ordine_cliente(self):
        # Crea una nuovo ordine cliente per il cliente "Cliente". *Required*
        importi = RowManager.list()
        #self.creazione_ordine_cliente("Cliente", importi[0])
        #self.creazione_ordine_cliente("Cliente", importi[0])

        # Modifica ordine cliente
        #self.modifica_ordine_cliente()

        # Cancellazione ordine cliente
        #self.elimina_ordine_cliente()

        # Verifica ordine cliente
        #self.verifica_ordine_cliente()

        # Plugin consuntivi
        #self.consuntivi()

        # Cambia stato (Azioni di gruppo)
        #self.cambia_stato()

        # Fattura ordini cliente (Azioni di gruppo)
        self.fattura_ordini_clienti()


    def creazione_ordine_cliente(self, cliente: str, file_importi: str):
        self.navigateTo("Ordini cliente")
        self.wait_loader() 

        # Crea un nuovo ordine cliente per il cliente indicato. 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto ordine cliente', toast)

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def modifica_ordine_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        sleep(2)
        
        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Accettato")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//button[@id="save"]'))).click()
        sleep(2)

        # Estrazione totali righe
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"]+ ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_ordine_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_ordine_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))).send_keys("Accettato", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[7]').text
        self.assertEqual("Accettato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def consuntivi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[2])[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_29"]').click()
        self.wait_loader()

        budget=self.find(By.XPATH, '(//div[@id="tab_29"]//span)[2]').text
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.assertEqual(budget, "+264,80 €")
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def cambia_stato(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]').click()  #click su tasto aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))).click()   #cambio stato in Accettato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Accettato', Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Ordini cliente")   #torna in pagina principale
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('02', Keys.ENTER) #cerco l'ordine 02     
        sleep(1)

        self.find(By.XPATH, '(//tr[1]//td[1])[2]').click()  #seleziono l'ordine
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[2]').click()   #click su cambia stato
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click() #seleziono nuovo stato (Fatturato)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Fatturato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su Procedi
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tbody//tr[1]//td[7]//span)[2]').text #controllo se lo stato è stato cambiato correttamente
        self.assertEqual(stato, "Fatturato")
        #elimino ordine
        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click() #cancello la ricerca
        sleep(2)

    def fattura_ordini_clienti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su tasto +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-primary"]').click()  #click su tasto aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys('Test') #aggiunta descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys('1')   #aggiunta prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoordine-container"]'))).click()   #cambio stato in Accettato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Accettato', Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[1])[2]').click()  #seleziono l'ordine
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[1]').click()   #click su fattura ordini cliente
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()   #ragruppa per cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click su procedi
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo=self.find(By.XPATH, '(//tr[1]//td[4]//div)[2]').text
        self.assertEqual(tipo, "Fattura immediata di vendita")  #controlla se è stata creata la fattura
        #elimina fattura
        self.find(By.XPATH, '(//tr[1]//td[4]//div)[2]').click()
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

