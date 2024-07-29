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


class Attivita(Test):
    def setUp(self):
        super().setUp()

       
    def test_attivita(self):
        # Crea un nuovo intervento. *Required*
        importi = RowManager.list()
        self.attivita("Cliente", "1", "2", importi[0])

        # Duplica attività
        self.duplica_attività()

        # Modifica intervento
        self.modifica_attività("3")

        # Cancellazione intervento
        self.elimina_attività()

        # Controllo righe
        self.controllo_righe()

        # Verifica attività
        self.verifica_attività()

        # Controllo storico attività plugin in Anagrafica
        self.storico_attivita()
        
        # Cambia stato (Azioni di gruppo)
        self.cambio_stato()

        # Duplica attività (Azioni di gruppo)
        self.duplica()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

        # Firma interventi (Azioni di gruppo)
        self.firma_interventi()

        # Fattura attività (Azioni di gruppo)
        self.fattura_attivita()

        # Stampa riepilogo (Azioni di gruppo)
        self.stampa_riepilogo()


    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")

        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")
        self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def duplica_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="pulsanti"]//button[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-results"]//li[2]'))).click()
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@type="submit"]').click()
        self.wait_loader()
    
    def modifica_attività(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Stato').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def controllo_righe(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()  
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        sleep(1)

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, (self.valori["Imponibile"] + ' €'))
        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale, (self.valori["Totale imponibile"]+ ' €'))


        imponibilefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale,imponibile)
        self.assertEqual(scontofinale,sconto)
        self.assertEqual(totaleimpfinale,totale)
        self.assertEqual(IVA, (self.valori["IVA"] + ' €'))
        self.assertEqual(totalefinale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def verifica_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[7]').text
        self.assertEqual("Fatturato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def storico_attivita(self):  
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_28"]').click() #apre pagina con tutte le attività
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_28"]//tbody//tr//td[1]') #se rileva il checkbox della attività il test è superato

    def cambio_stato(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)  #Cerca attività numero 1
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[1]').click()   #seleziona primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="cambia_stato"]'))).click()    #click su cambia stato
        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Da programmare") #seleziona stato "Da programmare"
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click primo risultato
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[7]//div)[2]').text
        self.assertEqual(stato, "Da programmare")   #controlla se lo stato è "Da programmare"
        #ritorno come era prima
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="cambia_stato"]'))).click()    #click su cambia stato
        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Programmato")    #seleziona stato "Programmato"
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click primo risultato
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        nuovo_stato=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[7]//div)[2]').text  #controlla se lo stato è "Programmato"
        self.assertEqual(nuovo_stato, "Programmato")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(2)

    def duplica(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)  #cerca attività numero 1
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziona prima attività
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="copy-bulk"]'))).click()   #click su duplica attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #seleziona stato "Da programmare"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Da programmare")
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click sul primo risultato
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)  #cerca attività numero 2
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[2])[2]')))   #controlla la presenza del attività
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()  #cancella ricerca
        sleep(2)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)  #cerca attività numero 2
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziona attività numero 2
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="delete-bulk"]'))).click() #click su elimina selezionati
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        scritta=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1])[4]').text  #controllo se è stata eliminata l'attività
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(2)    

    def firma_interventi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        #creo attività
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()
        sleep(2)

        #firmo attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziono prima attività
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="firma-intervento"]'))).click()    #click su firmo intervento
        sleep(1)

        self.find(By.XPATH, '//button[@id="firma"]').click()    #click su firma
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys("firma") #scrivo firma
        self.find(By.XPATH, '//button[@class="btn btn-success pull-right"]').click()    #click su Salva firma
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()    #apro attività
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="text-center row"]//div)[3]'))) #check firma

    def fattura_attivita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click sul primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="back"]').click() #torno in attività
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("3", Keys.ENTER)  #cerco attività numero 3
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono attività 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")  
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla prima fattura
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click() #elimina fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(2)    

    def stampa_riepilogo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("3", Keys.ENTER)  #cerco attività numero 3
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono attività 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="stampa-riepilogo"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        prezzo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[73]').text
        self.assertEqual(prezzo, "1,22 €")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() #elimino attività
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
