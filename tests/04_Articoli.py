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
        self.elimina_selezionati()      #da tenere come ultimo test delle azioni di gruppo

    def creazione_articolo(self, codice: str, descrizione: str):
        self.navigateTo("Articoli")
        self.wait_loader()
        # #
        # 1/2 Crea un nuovo articolo. 
        # #
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        # Submit
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
        sleep(2)  

    def elimina_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_articolo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[9]').text
        self.assertEqual("20,00",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        self.wait_loader()

        #verifica elemento eliminato
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
        
        self.find(By.XPATH, '(//label[@class="btn btn-default"])[1]').click()
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_11"]').click()
        sleep(1)
        self.find(By.XPATH, '//input[@id="serial_start"]').send_keys("1")
        sleep(1)
        self.find(By.XPATH, '//input[@id="serial_end"]').send_keys(Keys.BACK_SPACE, "2")
        sleep(1)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[3]').click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))).click()
        sleep(1)
        serial = self.find(By.XPATH, '//div[@id="tab_11"]//tbody//tr[2]//td[1]').text
        self.assertEqual(serial, "1")
        self.wait_loader()

        #elimina seriale e verifica eliminazione 
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
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_43"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_43"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idagente-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Agente", Keys.ENTER)
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("1.00", Keys.ENTER)
        sleep(2)
        self.wait_loader()
        
        self.find(By.XPATH, '//td[@class="  select-checkbox"]') #se trova il checkbox test superato
        #modifica provvigione
        self.find(By.XPATH, '(//div[@id="tab_43"]//tr[1]//td[2])[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("2", Keys.ENTER)
        self.wait_loader()

        provvigione=self.find(By.XPATH, '(//div[@id="tab_43"]//tr[1]//td[3]/div)[2]').text
        self.assertEqual(provvigione, "2.00 €")
        
        #eliminazione provvigione
        self.find(By.XPATH, '//td[@class="bound clickable"][1]').click()
        sleep(2)

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
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.wait_loader()

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

        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_fornitore-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER) 

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Articolo 1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click()
        self.wait_loader()

        nome=self.find(By.XPATH, '//div[@id="tab_32"]//tr//td[2]').text
        self.assertEqual(nome, "Articolo 1")
        #modifica
        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fornitore"]'))).send_keys(Keys.BACKSPACE,Keys.BACK_SPACE,"1", Keys.ENTER)
        self.wait_loader()

        codice=self.find(By.XPATH, '(//div[@id="tab_32"]//td[3])[1]').text
        self.assertEqual(codice,"01")

        #elimina
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

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_22"]').click()
        sleep(1)

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

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_10"]').click()
        sleep(2)

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

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_24"]').click()
        self.wait_loader()

        numero_1=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]').text
        self.assertEqual(numero_1, "1")

        numero_2=self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]').text
        self.assertEqual(numero_2, "1")
        sleep(2)

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

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_27"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_cliente_informazioni-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Cliente', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info btn-block"]').click()
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys('5', Keys.ENTER)
        sleep(2)
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_27"]//tr[3]//td[1]')))
        #modifica
        self.find(By.XPATH, '//button[@class="btn btn-xs btn-warning"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys(Keys.BACK_SPACE,'2', Keys.ENTER)
        sleep(2)
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//div[@id="tab_27"]//tr[3]//td[4]').text
        self.assertEqual(prezzo[0:6], "2,00 €")
        #eliminazione
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
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="titolo"]'))).send_keys('Taglie', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('S', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('M', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('L', Keys.ENTER)
        sleep(2)

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)

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

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]')))
        #modifica
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-warning btn-xs"])[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys(Keys.BACKSPACE,"XS",Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        taglia=self.find(By.XPATH, '//div[@id="tab_34"]//tr[1]//td[2]').text
        self.assertEqual(taglia, "Taglie: XS")
        #elimina
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tbody//tr[1]').text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def aggiorna_prezzo_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys("08")   #scrivo 08 come codice
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Prova")    #scrivo Prova come descrizione
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_acquisto"]'))).send_keys("1") #seleziono 1 come prezzo di acquisto
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))).send_keys("1") #seleziono 1 come prezzo di vendita
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()
        
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziono primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-acquisto"]').click() #click su aggiorna prezzo di acquisto
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("10")  #scrivo 10 come percentuale
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click su procedi
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr[1]//td[8]//div').text   #controllo se il prezzo è passato da 1 a 1,10
        self.assertEqual(prezzo, "1,10")
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)
        
    def aggiorna_prezzo_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-vendita"]').click() #click su aggiorna prezzo di vendita
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-prezzo_partenza-container"]').click() #seleziono il prezzo di vendita come prezzo di partenza
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Prezzo di vendita")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-prezzo_partenza-results"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("20") #seleziono 20 come percentuale
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click di conferma
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr[1]//td[9]//div').text
        self.assertEqual(prezzo, "0,98")    #controllo se il prezzo è diventato 0,98
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(1)

    def coefficiente_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #click sul primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-coefficiente"]').click()  #seleziono aggiorna coefficiente di vendita
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="coefficiente"]'))).send_keys("12") #seleziono 12 come coefficiente
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click di conferma
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr[1]//td[9]//div').text
        self.assertEqual(prezzo, "13,20")   #controllo se il prezzo è diventato 13,20
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)

    def aggiorna_quantita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-qta"]').click()   #click su aggiorna quantità
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("3") #scrivo 3 come quanità
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="descrizione"]'))).send_keys("test") #scrivo "test" come descrizione
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        quantita=self.find(By.XPATH, '//tbody//tr[1]//td[10]//div').text
        self.assertEqual(quantita, "3,00")  #controllo se la quantità è uguale a "3,00"
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(1)

    def crea_preventivo(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="crea-preventivo"]').click() #click su crea preventivo
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova") #scrivo "Prova" come nome
        self.find(By.XPATH, '//span[@id="select2-id_cliente-container"]').click() #seleziono "Cliente" come cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()   #seleziono "Standard preventivi" come sezionale
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard preventivi", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_tipo-container"]').click()  #seleziono "Generico" come tipo di attività
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Generico", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        #elimina preventivo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(1)
    def aggiorna_iva(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-iva"]').click() #seleziono aggiorna iva
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_iva-container"]').click()   #seleziono l'iva al 10%
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Iva 10%")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_iva-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro articolo
        self.wait_loader()

        iva=self.find(By.XPATH, '//span[@id="select2-idiva_vendita-container"]').text
        self.assertEqual(iva[2:20], "10 - Aliq. Iva 10%")   #controllo se l'iva è al 10%
        self.navigateTo("Articoli") #torno indietro
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancella ricerca
        sleep(1)

    def aggiorna_unita_misura(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-um"]').click() #seleziono aggiorna unità di misura
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-um-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("pz") #seleziono pz come unità di misura
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-um-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apri articolo
        self.wait_loader()

        unita_misura=self.find(By.XPATH, '//span[@id="select2-um-container"]').text
        self.assertEqual(unita_misura[2:5], "pz")   #controllo se pz è l'unità di misura

        self.navigateTo("Articoli") #torno indietro
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)

    def conto_predefinito_acquisto(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-conto-acquisto"]').click()  #seleziono aggiorna conto predefinito di acquisto
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-conto_acquisto-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fabbricati") #seleziono il conto "Fabbricati"
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-conto_acquisto-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro articolo
        self.wait_loader()

        conto=self.find(By.XPATH, '//span[@id="select2-idconto_acquisto-container"]').text
        self.assertEqual(conto[2:24], "220.000010 Fabbricati")  #controllo se il conto selezionato è quello dei Fabbricati
        sleep(2)

        self.navigateTo("Articoli") #torno indietro
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)

    def conto_predefinito_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-conto-vendita"]').click() #click su Aggiorna conto predefinito di vendita
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-conto_vendita-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Automezzi")  #seleziono conto "Automezzi"
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-conto_vendita-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro articolo
        self.wait_loader()

        conto=self.find(By.XPATH, '//span[@id="select2-idconto_vendita-container"]').text
        self.assertEqual(conto[2:24], "220.000030 Automezzi") #controllo se il conto è quello degli Automezzi
        sleep(2)

        self.navigateTo("Articoli") #torno indietro
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)

    def imposta_provvigione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="set-provvigione"]').click() #click su imposta provvigione
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-idagente-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Agente", Keys.ENTER) #seleziono "Agente" come agente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))).send_keys("10") #seleziono provvigione del 10%
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro articolo
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  #apro barra dei plugin
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_43"]').click()   #vado in Provvigioni
        sleep(1)

        provvigione=self.find(By.XPATH, '(//div[@id="tab_43" ]//tr[1]//td[3]//div)[2]').text
        self.assertEqual(provvigione, "10.00 %")    #controllo se la provvigione è del 10%

        self.navigateTo("Articoli") #torno indietro
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(1)

    def aggiorna_prezzo_unitario(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #click su articolo
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  #apro barra dei plugin
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click() #apro plugin listino fornitori
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_fornitore_informazioni-container"]').click()    #seleziono "Fornitore" come fornitore
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-info"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))).send_keys("100") #seleziono 100 come quantità minima
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))).send_keys("15")  #seleziono 15 come giorni di consegna
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))).send_keys("15", Keys.ENTER)    #seleziono 15 come prezzo unitario
        self.wait_loader()

        self.navigateTo("Listini")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono primo listino
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change_prezzo"]').click() #click su aggiorna prezzo unitario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))).send_keys("20") #seleziono 20 come percentuale
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        self.wait_loader()

        prezzo=self.find(By.XPATH, '(//tr[1]//td[8])[2]').text  #controllo se il prezzo è cambiato
        self.assertEqual(prezzo, "18,00")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #deseleziono primo listino
        sleep(1)

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #elimina ricerca
        sleep(1)

    def copia_listini(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Listini")
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()  #vado in sezionale "Fornitori"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitori")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono primo listino
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="copy_listino"]').click() #click su copia listini
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys("Estero")
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #tolgo checkbox
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="form-control"])[2]'))).send_keys("Fornitore Estero", Keys.ENTER)
        sleep(2)

        articolo=self.find(By.XPATH, '(//tr[1]//td[2]//div)[2]').text #controllo se è stato creato il listino
        self.assertEqual(articolo, "08 - Prova")
        sleep(2)

        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #click su articolo
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()  #apro barra dei plugin
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_32"]').click() #apro plugin listino fornitori
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-secondary btn-danger ask"]').click() #elimino listino fornitore
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-warning"]').click() #elimino listino fornitore estero
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #elimina ricerca
        sleep(1)

    def imposta_prezzo_da_fattura(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys("09")   #scrivo 09 come codice
        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Test")    #scrivo Test come descrizione
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        
        self.navigateTo("Articoli")
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("04")   #scrivo 04 come numero esterno
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono "Fornitore" come fornitore
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').click() #aggiungi pagamento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Assegno")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungi articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field" ]'))).send_keys("Test")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field" ]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-xs btn-warning"]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")   #imposta prezzo a 1
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        sleep(2)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("09", Keys.ENTER) #cerco l'articolo con il codice 09
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono articolo
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="set-acquisto-ifzero"]').click() #click su imposta prezzo di acquisto da fattura
        sleep(2)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click di conferma
        self.wait_loader()

        prezzo=self.find(By.XPATH, '//tbody//tr//td[8]').text #controllo se il prezzo è cambiato
        self.assertEqual(prezzo, "1,00")

        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() #cancella ricerca
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="bound clickable"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

    def stampa_etichette(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="form-control"])[2]'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr/td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="stampa-etichette"]').click() #click su stampa etichette
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(1)

        prezzo=self.find(By.XPATH, '(//div[@id="viewer"]//span)[3]').text
        self.assertEqual(prezzo, "13,20 €") #check del etichetta
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)

        self.find(By.XPATH, '(//tr[1]//td[1])[2]').click() #tolgo selezione
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() #cancella ricerca
        sleep(1)


    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("08", Keys.ENTER) #cerco l'articolo con il codice 08
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono il primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #click su azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click() #click su elimina selezionati
        sleep(2)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        risultato=self.find(By.XPATH, '//tbody//tr//td').text #controlla se appare la scritta e quindi se è stato eliminato l'articolo
        self.assertEqual(risultato, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//th[@id="th_Codice"]/i[@class="deleteicon fa fa-times"]').click() #elimina ricerca
        sleep(1)