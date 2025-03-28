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

class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Acquisti")

    def test_creazione_fattura_acquisto(self):
        # Crea una nuova fattura *Required*
        importi = RowManager.list()
        self.creazione_fattura_acquisto("Fornitore", "1", "1", importi[0])

        # Modifica fattura
        self.modifica_fattura_acquisto("Emessa")
        
        # Controllo valori piano dei conti
        self.controllo_fattura_acquisto()

        # Cancellazione fattura di acquisto
        self.elimina_documento()

        # Verifica fattura di acquisto
        self.verifica_fattura_acquisto()

        # Verifica XML autofattura
        self.verifica_xml_autofattura(importi[0], "1")

        # Plugin Registrazioni
        self.registrazioni()

        # Plugin movimenti contabili
        self.movimenti_contabili()

        # Cambia sezionale (Azioni di gruppo)
        self.cambia_sezionale()

        # Duplica selezionati (Azioni di gruppo)
        self.duplica_selezionati()

        # Registrazione contabile (Azioni di gruppo)
        self.registrazione_contabile()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

    def creazione_fattura_acquisto(self, fornitore: str, numero: str, pagamento: str, file_importi: str):
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        # Crea fattura
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'N. fattura del fornitore').setValue(numero)
        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento')
        select.setByIndex(pagamento)
        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def modifica_fattura_acquisto(self, modifica=str):
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Stato*').setByText(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

    def controllo_fattura_acquisto(self):
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        # Estrazione totali righe
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, self.valori["Sconto/maggiorazione"]+ ' €')
        self.assertEqual(totale_imponibile, self.valori["Totale imponibile"]+ ' €')
        self.assertEqual(iva, self.valori["IVA"] + ' €')
        self.assertEqual(totale, self.valori["Totale documento"] + ' €')

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:21])
        self.driver.execute_script('$("a").removeAttr("target")')
        self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a').click()
        self.wait_loader()

        totale = '-'+ totale
        scadenza_scadenzario = (self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text + ' €')
        self.assertEqual(totale, scadenza_scadenzario)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        # Estrazione Totale widgets
        widget_fatturato = self.find(By.XPATH, '(//span[@class="info-box-number"])[1]').text
        widget_crediti = self.find(By.XPATH, '(//span[@class="info-box-number"])[2]').text
        widget_crediti='-'+widget_crediti

        # Confronto i due valori
        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)

        # Estrazione valori Piano dei conti
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")
        self.wait_loader()

        self.find(By.XPATH, '//*[@id="conto2-14"]//*[@class="fa fa-plus"]').click()
        sleep(1) 
        self.find(By.XPATH, '//*[@id="movimenti-55"]//*[@class="fa fa-plus"]').click()
        sleep(1) 
        conto_costi = self.find(By.XPATH, '//*[@id="conto_55"]//*[@class="text-right"]').text
       
        self.find(By.XPATH, '//*[@id="conto2-8"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-122"]//*[@class="fa fa-plus"]').click()
        sleep(1) 
        conto_fornitore = self.find(By.XPATH, '//*[@id="conto_122"]//*[@class="text-right"]').text
        conto_fornitore='-'+conto_fornitore

        self.find(By.XPATH, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-107"]//*[@class="fa fa-plus"]').click()        
        sleep(1) 
        conto_iva = self.find(By.XPATH, '//*[@id="conto_107"]//*[@class="text-right"]').text

        self.assertEqual(totale_imponibile, conto_costi)
        self.assertEqual(totale, conto_fornitore)
        self.assertEqual(iva, conto_iva)

    def elimina_documento(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

    def verifica_fattura_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()  

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella",eliminato)

        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() 
        sleep(1)

    def verifica_xml_autofattura(self, file_importi: str, pagamento: str):
        wait = WebDriverWait(self.driver, 20)
    
        # Creazione fattura di acquisto estera
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()  

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText("Fornitore Estero")
        sleep(1)

        self.input(modal, 'N. fattura del fornitore').setValue("01")
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento')
        select.setByIndex(pagamento)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)    
        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        sleep(1)

        # Creazione autofattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary unblockable dropdown-toggle "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="btn dropdown-item bound clickable"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("TD17")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//button[@type="submit"]'))).click()
        self.wait_loader()

      
        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text

        self.assertEqual(totale_imponibile, ('0,00 €'))
        self.assertEqual(totale, ('0,00 €'))

    def registrazioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="link-tab_41"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_41"]//tr[5]//td[1]'))) 
    def movimenti_contabili(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()


        self.find(By.XPATH, '//a[@id="link-tab_36"]').click()
        self.find(By.XPATH, '//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader()

        avere=self.find(By.XPATH, '//div[@id="tab_36"]//tr//td[4]').text
        self.assertEqual(avere,"323,06 €")

    def cambia_sezionale(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("2")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.navigateTo("Fatture di acquisto") 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Autofatture")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Autofatture")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click() 
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click()
        self.wait_loader()

    def duplica_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[1]').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        self.find(By.XPATH, '//a[@data-op="copy-bulk"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()  
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()  
        self.wait_loader()

    def registrazione_contabile(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("2")
        self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Assegno")
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Prova") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")   
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER) 
        self.find(By.XPATH, '//button[@id="save"]').click() 
        self.wait_loader()

        self.navigateTo("Fatture di acquisto") 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="registrazione-contabile"]').click()
        sleep(1)

        # TODO: Selezionare il conto Banca C/C e aggiungere la registrazione contabile

        prezzo=self.find(By.XPATH, '//th[@id="totale_avere"]').text
        self.assertEqual(prezzo, "1,22 €")
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() 
        sleep(1)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)