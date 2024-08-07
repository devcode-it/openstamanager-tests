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


class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_creazione_articolo(self):
        # Crea un nuovo articolo. *Required*
        self.creazione_articolo("002", "Articolo di Prova")
        self.creazione_articolo("003", "Articolo di Prova da Eliminare")
        
        # Modifica articolo
        self.modifica_articolo("20", "1", "2", "carico di test")
        
        # Cancellazione articolo
        self.elimina_articolo()
        
        # Verifica articolo
        self.verifica_articolo()

        # Plugin seriali
        self.serial()

        # Plugin provvigioni
        self.provvigioni()

        # Plugin listino fornitori
        self.listino_fornitori()

        # Plugin giacenze
        self.giacenze()

        # Plugin movimenti
        self.plugin_movimenti()

        # Plugin statistiche
        self.statistiche()

        # Plugin netto clienti
        self.netto_clienti()

        # Plugin varianti articoli
        self.varianti_articoli()

        # Aggiorna prezzo di acquisto (Azioni di gruppo)
        self.aggiorna_prezzo_acquisto()

        # Aggiorna prezzo di vendita (Azioni di gruppo)
        self.aggiorna_prezzo_vendita()

        # Aggiorna coefficiente di vendita (Azioni di gruppo)
        self.coefficiente_vendita()

        # Aggiorna quantità (Azioni di gruppo)
        self.aggiorna_quantita()

        # Crea preventivo (Azioni di gruppo)
        self.crea_preventivo()

        # Aggiorna aliquota iva (Azioni di gruppo)
        self.aggiorna_iva()

        # Aggiorna unità di misura (Azioni di gruppo)
        self.aggiorna_unita_misura()

        # Aggiorna conto predefinito di acquisto (Azioni di gruppo)
        self.conto_predefinito_acquisto()

        # Aggiorna conto predefinito di vendita (Azioni di gruppo)
        self.conto_predefinito_vendita()

        # Imposta una provvigione (Azioni di gruppo)
        self.imposta_provvigione()

        # Aggiorna prezzo unitario (Azioni di gruppo) da Listini
        self.aggiorna_prezzo_unitario()

        # Copia listini (Azioni di gruppo) da Listini
        self.copia_listini()

        # Imposta prezzo di acquisto da fattura (Azioni di gruppo)
        self.imposta_prezzo_da_fattura()

        # Stampa etichette (Azioni di gruppo)
        self.stampa_etichette()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()      

    def creazione_articolo(self, codice: str, descrizione: str):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       
    def modifica_articolo(self, acquisto:str, coefficiente:str, qta: str, descrizione: str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.input(None, 'Prezzo di acquisto').setValue(acquisto)
        self.input(None, 'Coefficiente').setValue(coefficiente)

        self.find(By.XPATH, '//div[@class="btn-group checkbox-buttons"]//label[@for="qta_manuale"]').click()
        self.input(None, 'Quantità').setValue(qta)
        self.input(None, 'Descrizione').setValue(descrizione)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        sleep(1)

        # Controllo quantità 
        self.find(By.XPATH, '//a[@id="back"]').click()
        sleep(1)
        
        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, "2,00")

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)  

    def elimina_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[9]').text
        self.assertEqual("20,00",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Articolo di prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def serial(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        # Abilito l'inserimento di serial
        self.find(By.XPATH, '//label[@for="abilita_serial"]').click()
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        # Aggiungo serial
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_11"]').click()
        self.find(By.XPATH, '//input[@id="serial_start"]').send_keys("1")
        self.find(By.XPATH, '//input[@id="serial_end"]').send_keys(Keys.BACK_SPACE, "2")
        self.find(By.XPATH, '//div[@id="tab_11"]//button[@type="button"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))).click()
        sleep(1)

        # Verifico serial
        serial = self.find(By.XPATH, '//div[@id="tab_11"]//tbody//tr[2]//td[1]').text
        self.assertEqual(serial, "1")
        self.wait_loader()

        # TODO: Inserimento singolo serial

        # Elimina serial
        self.find(By.XPATH, '(//a[@class="btn btn-danger btn-sm ask"])[2]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()  

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@id="tab_11"]//tbody//tr[2]//td[1]'))) 

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def provvigioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_43"]').click()
        self.find(By.XPATH, '//div[@id="tab_43"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        # Aggiunta provvigione
        self.find(By.XPATH, '//span[@id="select2-idagente-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Agente", Keys.ENTER)
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("1.00", Keys.ENTER)
        self.wait_loader()
        
        # TODO: Verifica provvigione -> Questa provvigione viene impostata all'aggiunta di questo articolo in un documento dove è impostato come Agente questo agente. Creare una fattura di vendita con agente Agente e aggiungere Articolo 001 alle righe. 

        self.find(By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[2]').click()
        self.wait_modal()

        # Modifica provvigione
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("2", Keys.ENTER)
        self.wait_loader()

        provvigione=self.find(By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[3]').text
        self.assertEqual(provvigione, "2.00 €")
        
        # Elimina provvigione
        self.find(By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[3]').click()
        sleep(1)

        self.find(By.XPATH, '(//a[@class="btn btn-danger ask"])[2]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()
        
        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def listino_fornitori(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()

        # Aggiungo listino fornitore
        self.find(By.XPATH, '//span[@id="select2-id_fornitore_informazioni-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))).send_keys("15")
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys("15", Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_fornitore-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER) 

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        # TODO: Verifica listino fornitore -> Creo una fattura di acquisto impostando come fornitore Fornitore, aggiungendo questo articolo alle righe deve impostarsi il corretto prezzo di acquisto e lo sconto qui definito.

        # Modifica listino fornitore
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fornitore"]'))).send_keys(Keys.BACKSPACE,Keys.BACK_SPACE,"1", Keys.ENTER)
        self.wait_loader()

        codice=self.find(By.XPATH, '//div[@id="tab_32"]//tbody//tr//td[3]').text
        self.assertEqual(codice,"01")

        # Elimina listino fornitore
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-danger ask"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        messaggio=self.find(By.XPATH, '(//div[@class="alert alert-info"])[5]').text
        self.assertEqual(messaggio, "Nessuna informazione disponibile...")
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def giacenze(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_22"]').click()

        # Verifico giacenze
        totale=self.find(By.XPATH, '//div[@id="tab_22"]//tbody//tr//td[2]').text
        self.assertEqual(totale, "3,00")
        self.find(By.XPATH, '//a[@class="btn btn-xs btn-info"]').click()
        sleep(1)

        totale_2=self.find(By.XPATH, '(//div[@id="tab_22"]//div[@class="col-md-12 text-center"])[2]').text
        self.assertEqual(totale_2, "3,00")
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_movimenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        # Verifico plugin movimenti
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_10"]').click()
        quantita=self.find(By.XPATH, '(//div[@id="tab_10"]//div[2]//b)[4]').text
        self.assertEqual(quantita, "3,00")

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def statistiche(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_24"]').click()

        # Verifico statistiche
        numero_1=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]').text
        self.assertEqual(numero_1, "1")

        numero_2=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]').text
        self.assertEqual(numero_2, "1")

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def netto_clienti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_27"]').click()

        # Aggiungo listino cliente
        self.find(By.XPATH, '//span[@id="select2-id_cliente_informazioni-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Cliente', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info btn-block"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys('5', Keys.ENTER)
        self.wait_loader()

        # TODO: Verifica listino cliente -> Creo una fattura di vendita impostando come cliente Cliente, aggiungendo questo articolo alle righe deve impostarsi il corretto prezzo di vendita e lo sconto qui definito.

        # Modifica listino cliente
        self.find(By.XPATH, '//button[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys(Keys.BACK_SPACE,'2', Keys.ENTER)
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//div[@id="tab_27"]//tr[3]//td[4]').text
        self.assertEqual(prezzo[0:6], "2,00 €")

        # Elimina listino cliente
        self.find(By.XPATH, '//button[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default"])[4]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//div[@id="tab_27"]//div[@class="alert alert-info"]').text
        self.assertEqual(messaggio,"Nessuna informazione disponibile...")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def varianti_articoli(self):
        # TODO: Ottimizzare spostando nel test Combinazioni

        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        # Creazione Attributi
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="titolo"]'))).send_keys('Taglie', Keys.ENTER)
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="aggiungiValore(this)"]'))).click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('S', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('M', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('L', Keys.ENTER)
        sleep(1)

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Creazione combinazioni
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys('001')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Vestito')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys('Taglie', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-warning "]').click()
        self.wait_loader()

        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        # Verifica combinazioni
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]')))

        # Modifica combinazioni
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-warning btn-xs"])[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys(Keys.BACKSPACE,"XS",Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        taglia=self.find(By.XPATH, '//div[@id="tab_34"]//tr[1]//td[2]').text
        self.assertEqual(taglia, "Taglie: XS")

        # Elimina attributi
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr[1]').text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")

        # TODO: Elimina combinazioni.

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def aggiorna_prezzo_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        # Creo articolo
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys("08") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Prova")   
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_acquisto"]'))).send_keys("1") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))).send_keys("1") 
        self.find(By.XPATH, '//button[@id="save"]').click() 
        self.wait_loader()
        
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        self.find(By.XPATH, '//a[@data-op="change-acquisto"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("10") 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr//td[8]').text
        self.assertEqual(prezzo, "1,10")
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def aggiorna_prezzo_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        self.find(By.XPATH, '//a[@data-op="change-vendita"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-prezzo_partenza-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Prezzo di vendita")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-prezzo_partenza-results"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("20") 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr//td[9]').text
        self.assertEqual(prezzo, "0,98")  
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def coefficiente_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  
        self.find(By.XPATH, '//a[@data-op="change-coefficiente"]').click() 
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="coefficiente"]'))).send_keys("12") 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr[1]//td[9]//div').text
        self.assertEqual(prezzo, "13,20") 
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def aggiorna_quantita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        self.find(By.XPATH, '//a[@data-op="change-qta"]').click() 
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("3") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="descrizione"]'))).send_keys("test")
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        quantita=self.find(By.XPATH, '//tbody//tr//td[10]').text
        self.assertEqual(quantita, "3,00")  
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def crea_preventivo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="crea-preventivo"]').click() 
        sleep(1)

        # Crea preventivo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova") 
        self.find(By.XPATH, '//span[@id="select2-id_cliente-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard preventivi", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_tipo-container"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Generico", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        # Elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)
    
    def aggiorna_iva(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        self.find(By.XPATH, '//a[@data-op="change-iva"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_iva-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Iva 10%")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_iva-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        iva=self.find(By.XPATH, '//span[@id="select2-idiva_vendita-container"]').text
        self.assertEqual(iva[2:20], "10 - Aliq. Iva 10%")  
        self.navigateTo("Articoli") 
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def aggiorna_unita_misura(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="change-um"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-um-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("pz")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-um-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        unita_misura=self.find(By.XPATH, '//span[@id="select2-um-container"]').text
        self.assertEqual(unita_misura[2:5], "pz")  

        self.navigateTo("Articoli") 
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def conto_predefinito_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="change-conto-acquisto"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-conto_acquisto-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fabbricati")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-conto_acquisto-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()

        conto=self.find(By.XPATH, '//span[@id="select2-idconto_acquisto-container"]').text
        self.assertEqual(conto[2:24], "220.000010 Fabbricati") 
        sleep(1)

        self.navigateTo("Articoli") 
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def conto_predefinito_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="change-conto-vendita"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-conto_vendita-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Automezzi")  
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-conto_vendita-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        conto=self.find(By.XPATH, '//span[@id="select2-idconto_vendita-container"]').text
        self.assertEqual(conto[2:24], "220.000030 Automezzi") 
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def imposta_provvigione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="set-provvigione"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idagente-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Agente", Keys.ENTER) 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("10") 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_43"]').click()  
        provvigione=self.find(By.XPATH, '(//div[@id="tab_43" ]//tr[1]//td[3]//div)[2]').text
        self.assertEqual(provvigione, "10.00 %")   

        self.navigateTo("Articoli") 
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def aggiorna_prezzo_unitario(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click() 
        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.find(By.XPATH, '//span[@id="select2-id_fornitore_informazioni-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))).send_keys("100") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))).send_keys("15")
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys("15", Keys.ENTER) 
        self.wait_loader()

        self.navigateTo("Listini")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="change_prezzo"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("20")
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        prezzo=self.find(By.XPATH, '(//tr[1]//td[8])[2]').text
        self.assertEqual(prezzo, "18,00")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

    def copia_listini(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Listini")
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitori")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="copy_listino"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys("Estero")
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Fornitore Estero", Keys.ENTER)
        sleep(1)

        articolo=self.find(By.XPATH, '//tbody//tr//td[2]').text
        self.assertEqual(articolo, "08 - Prova")
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-warning"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def imposta_prezzo_da_fattura(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("04")  
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Assegno")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field" ]'))).send_keys("Articolo di Prova")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field" ]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("10")  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("002", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="set-acquisto-ifzero"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr//td[8]').text
        self.assertEqual(prezzo, "10,00")

        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click()
        sleep(1)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Magazzino")

    def stampa_etichette(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr/td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="stampa-etichette"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        prezzo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[3]').text
        self.assertEqual(prezzo, "13,20 €") 
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        sleep(1)

        self.find(By.XPATH, '(//tr[1]//td[1])[2]').click() 
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() 
        sleep(1)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        risultato=self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(risultato, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)
