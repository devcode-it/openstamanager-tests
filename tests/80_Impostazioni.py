from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni(self):
        # Cambio cifre decimali per importi (Generali)
        self.cifre_decimali_importi()

        # Cambio valuta (Generali)
        self.valuta()

        # Cambio periodo calendario (Generali)
        self.periodo_calendario()

        # Cambio lingua (Generali)
        self.lingua()

        # Nascondere la barra sinistra di default (Generali)
        self.nascondi_barra_sx()

        # Cambio formato codice anagrafiche (Anagrafiche)
        self.cambio_formato_codice()

        # Mostra i prezzi al tecnico (Attività)
        self.mostra_prezzi_tecnico()

        # Permetti inserimento sessioni degli altri tecnici (Attività)
        self.inserimento_sessioni_tecnici()

        # Stato dell’attività dopo la firma (Attività)
        self.stato_attivita_firma()

        # Espandi automaticamente la sezione “Dettagli aggiuntivi” (Attività)
        self.espandi_barra_dettagli_aggiuntivi()

        # Verifica numero intervento (Attività)
        self.verifica_numero_intervento()

        # Stato predefinito dell'attività da Dashboard (Attività)
        self.stato_predefinito_attivita_dashboard()

        # Stato predefinito dell'attività (Attività)
        self.stato_predefinito_attivita()

        # Alert occupazione tecnici (Attività)
        self.alert_occupazione_tecnici()

        # Descrizione personalizzata in fatturazione (Attività)
        self.descrizione_fatturazione()

        # Condizioni generali di fornitura contratti (Contratti)
        self.condizioni_generali_contratti()

        # Crea contratto rinnocabile di default (Contratti)
        self.crea_contratto_rinnovabile()

        # Giorni di preavviso di default (Contratti)
        self.giorni_preavviso()

        # Cambia automaticamente stato ddt fatturati (Ddt)
        self.cambia_stato_ddt_fatturati()

        # Stato dell'attività dopo la firma (Attività)
        self.stato_attivita_firma()

        # Formato ore in stampa (Attività)
        self.formato_ore_stampa()

        # Visualizzare domenica sul calendario (Dashboard)
        self.visualizzare_domenica_calendario()

        # Ora inizio sul calendario (Dashboard)
        self.ora_inizio_calendario()

        # Ora fine sul calendario (Dashboard)
        self.ora_fine_calendario()

        # Visualizza informazioni aggiuntive sul calendario (Dashboard)
        self.visualizza_informazioni_aggiuntive()

        # Iva predefinita (Fatturazione)
        self.iva_predefinita()

    def cifre_decimali_importi(self):
        wait = WebDriverWait(self.driver, 20)
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        importo=self.find(By.XPATH, '//tbody//tr[1]//td[9]').text   #controllo se l'importo corrisponde a 20 euro con 4 cifre decimali
        self.assertEqual(importo, "20,0000 €")

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def valuta(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in sterline
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Sterlina', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro prima fattura
        self.wait_loader()

        nuova_valuta=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div//span').text   #controllo se è cambiata la valuta
        self.assertEqual(nuova_valuta, "£")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in euro
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Euro', Keys.ENTER)
        sleep(1)

    def periodo_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("30/06/2024", Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        data=self.find(By.XPATH, '//a[@class="nav-link text-danger"]').text #controllo se la data è cambiata
        self.assertEqual(data, "01/01/2024 - 30/06/2024")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("31/12/2024", Keys.ENTER)
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

    def lingua(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in inglese
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('English')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        scritta=self.find(By.XPATH, '(//li[@id="2"]//p)[1]').text   #controllo se ha cambiato lingua
        self.assertEqual(scritta, "Entities")
        #torno alle impostazioni di prima
        self.expandSidebar("Tools")
        self.navigateTo("Settings")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in italiano
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Italiano')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Settings")
        self.wait_loader()
        sleep(2)

    def nascondi_barra_sx(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #attivo impostazione
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        sleep(2)

        self.find(By.XPATH, '//body[@class="sidebar-mini layout-fixed  sidebar-collapse"]') #controlla se trova la classe sidebar-collapse
        #torno alle impostazioni di prima
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[1]').click() #disattivo impostazione
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        sleep(1)


    def cambio_formato_codice(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-1"]').click() #apro Anagrafiche
        sleep(1)

        formato=self.find(By.XPATH, '//input[@id="setting29"]') #cambio formato
        formato.clear()
        formato.send_keys("####", Keys.ENTER) #metto il formato a 4#
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(2)
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[5]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        codice_element = self.find(By.XPATH, '//input[@id="codice"]')   #controllo se il codice ha formato 4
        codice = codice_element.get_attribute("value")
        self.assertEqual(codice, "0010")  
        
        #elimino anagrafica
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-1"]').click() #apro Anagrafiche
        sleep(1)

        formato=self.find(By.XPATH, '//input[@id="setting29"]') #cambio formato
        formato.clear()
        formato.send_keys("#######", Keys.ENTER) #metto il formato a 7#
        sleep(2)

    def mostra_prezzi_tecnico(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #disattivo impostazione mostra prezzi al tecnico
        sleep(1)

        self.navigateTo("Utenti e permessi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]//input'))).send_keys('Tecnici', Keys.ENTER)   #cerca utente tecnici
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro primo risultato
        self.wait_loader()           

        self.find(By.XPATH, '//a[@class="pull-right btn btn-primary bound clickable"]').click() #aggiungi utente
        sleep(1)
        #imposto user
        user=self.find(By.XPATH, '//input[@id="username"]') 
        user.clear()
        user.send_keys("tecnicotest")
        #collego anagrafica
        self.find(By.XPATH, '//span[@id="select2-idanag-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Tecnico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        #imposto password
        password=self.find(By.XPATH, '//input[@id="password"]') 
        password.clear()
        password.send_keys("tecnicotest")
        self.find(By.XPATH, '//button[@id="submit-button"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//tbody//tr[17]//span)[2]').click() #aggiungo permessi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Lettura e scrittura')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('tecnicotest')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('tecnicotest') 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click() #aggiungi articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]')))  #controllo se non c'è la colonna degli importi
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da inserire al momento del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #attivo impostazione mostra prezzi al tecnico
        sleep(1)

    def inserimento_sessioni_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #attiva impostazione inserimento sessioni tecnici
        sleep(1)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('tecnicotest')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('tecnicotest') 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        #apro assegnazione tecnici
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"]//li)[3]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))) #controlla se appare tra le opzioni di scelta il tecnico
        #apro sessioni di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))) #controlla se appare tra le opzioni di scelta il tecnico
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        #chiudo
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(2)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da inserire al momento del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattiva impostazione inserimento sessioni tecnici
        sleep(1)
    
    def stato_attivita_firma(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Fatturato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '(//tbody//tr//td)[1]').click()  #seleziono prima attività
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro Azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="firma-intervento"]'))).click()    #click su firmo intervento
        sleep(1)

        self.find(By.XPATH, '//button[@id="firma"]').click()    #click su firma
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys("firma") #scrivo firma
        self.find(By.XPATH, '//button[@class="btn btn-success pull-right"]').click()    #click su Salva firma
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7]//div)[2]').text  #controllo se lo stato dopo la firma è Fatturato
        self.assertEqual(stato, "Fatturato")
        #elimino attività
        self.find(By.XPATH, '(//tbody//tr//td[2])[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        sleep(2)
        
    def espandi_barra_dettagli_aggiuntivi(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click() #attivo impostazione espandi automaticamente Dettagli aggiuntivi
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_scadenza"]')))    #controllo se gli elementi della barra sono visibili
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudo
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)
        
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click() #disattivo impostazione espandi automaticamente Dettagli aggiuntivi
        sleep(1)

    def verifica_numero_intervento(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        codice=self.find(By.XPATH, '//input[@id="codice"]') #cambio codice
        codice.clear()
        codice.send_keys("9")
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]'))) #check se appare l'alert
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() #elimino attività
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 
        
    def stato_predefinito_attivita_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting170-container"]').click()   #cambio lo stato predefinito a completato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '(//td[@class="fc-timegrid-slot fc-timegrid-slot-lane fc-timegrid-slot-minor"])[41]').click()   #click in calendario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #aggiunta tecnico
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))) #controlla se appare tra le opzioni di scelta il tecnico
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7])[2]').text
        self.assertEqual(stato, "Completato")
        #elimino attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting170-container"]').click()   #cambio lo stato predefinito a Programmato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def stato_predefinito_attivita(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting171-container"]').click()   #cambio lo stato predefinito a completato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7])[2]').text
        self.assertEqual(stato, "Completato")
        #elimino attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting171-container"]').click()   #cambio lo stato predefinito a Da Programmare
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Da programmare')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def alert_occupazione_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #cambio lo stato in "Programmato"
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #sessione di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click() #apro sessione di lavoro
        sleep(1)

        #orario inizio
        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")     #data di inizio 31/12/2024 09:00
        #orario fine
        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")     #data di fine 31/12/2024 10:00
        #tencico assegnato
        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click() #assegno il tecnico "Tecnico"
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        #faccio un'altra attività uguale
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('prova')
        #cambio lo stato in "Programmato"
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #sessione di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click() #apro sessione di lavoro
        sleep(1)

        #orario inizio
        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")     #data di inizio 31/12/2024 09:00
        #orario fine
        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")     #data di fine 31/12/2024 10:00
        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click() #tencico assegnato
        sleep(2)
        #assegno il tecnico "Tecnico"
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(2)
        #controllo se appare l'alert
        scritta=self.find(By.XPATH, '//div[@class="card-header"]//h3').text
        self.assertEqual(scritta, "⚠️ Sono presenti dei conflitti con le sessioni di lavoro di alcuni tecnici")
        self.find(By.XPATH, '//button[@class="close"]').click() #esco
        sleep(1)
        #elimino prima attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 
        sleep(1)

    def descrizione_fatturazione(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="setting155"]'))).send_keys("Intervento numero {numero} del {data_richiesta}")
        sleep(1)


        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #cambio lo stato in "Completato"
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[1]').click()   #seleziona prima attività
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apre Azioni di gruppo
        sleep(1)
        #apro fattura attività
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()   #ragruppa per cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()
        
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")  
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla prima fattura
        self.wait_loader()

        descrizione=self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual(descrizione[8:32], "Intervento numero 4 del ")   #da migliorare aggiungendo controllo sulla data
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click() #elimina fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #elimino attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        impostazione=self.find(By.XPATH, '//textarea[@id="setting155"]')
        impostazione.clear()
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        sleep(2)


    def condizioni_generali_contratti(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
        #scrivo Prova come scritta per condizioni generali 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).send_keys("Prova")
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()
        sleep(1)
        #creo contratto
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2024")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2024")
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        
        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #click su stampa contratto
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        scritta=self.find(By.XPATH, '//span[@style="left: 5.71%; top: 13.88%; font-size: calc(var(--scale-factor)*8.50px); font-family: sans-serif; transform: scaleX(0.913535);"]').text
        self.assertEqual(scritta, "Prova")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimino contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
        #torno alle impostazioni di prima
        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]').click()   #cancello la descrizione "Prova"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))).send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        sleep(2)
        
    def crea_contratto_rinnovabile(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #attivo impostazione
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-tool"]').click()  #click su informazioni per rinnovo
        sleep(1)

        stato=self.find(By.XPATH, '//label[@class="btn btn-default active"]//span[1]').text #check per vedere se il rinnovo è attivato
        self.assertEqual(stato, "Attivato")

        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #disattivo impostazione
        sleep(1)

    def giorni_preavviso(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
  
        giorni=self.find(By.XPATH, '//input[@id="setting192"]') #imposto i giorni di preavviso a 3
        giorni.clear()
        giorni.send_keys("3", Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-tool"]').click()  #click su informazioni per rinnovo
        sleep(1)

        giorni_element = self.find(By.XPATH, '//input[@id="giorni_preavviso_rinnovo_add"]')   #controllo se i giorni di preavviso sono 3
        giorni = giorni_element.get_attribute("value")
        self.assertEqual(giorni, "3,00")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)
  
        giorni=self.find(By.XPATH, '//input[@id="setting192"]') #imposto i giorni di preavviso a 2
        giorni.clear()
        giorni.send_keys("2", Keys.ENTER)
        sleep(1)

    def cambia_stato_ddt_fatturati(self):
        wait = WebDriverWait(self.driver, 20) 
        self.expandSidebar("Magazzino") #prima test con il ddt in entrata
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono "Admin spa" come mittente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()   #seleziono "Conto lavorazione" come causale
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su procedi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #seleziono primo ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[2]').click()   #click su fattura ddt
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #ragruppa per Cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text    #controllo se lo stato è in fatturato
        self.assertEqual(stato, "Fatturato")
        #elimino ddt
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino fattura
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla fattura in prima riga
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Magazzino") #test con il ddt in uscita
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +
        sleep(1)
        #seleziono destinatario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        #seleziono causale trasporto
        self.find(By.XPATH, '//span[@id="select2-idcausalet-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click() #cambio stato in evaso
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[1]').click()    #seleziono primo ddt
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[2]').click()   #click su fattura ddt
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #ragruppa per Cliente
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato2=self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text    #controllo se lo stato è in fatturato
        self.assertEqual(stato2, "Fatturato")
        #elimino ddt
        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        #elimino fattura
        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla fattura in prima riga
        self.wait_loader()
    
        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

    def stato_attivita_firma(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click() #seleziono stato "Fatturato"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Fatturato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click() #firma
        sleep(1)

        self.find(By.XPATH, '//button[@id="firma"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys('Prova')
        self.find(By.XPATH,'//button[@class="btn btn-success pull-right"]').click()
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7]//div)[2]').text
        self.assertEqual(stato, "Fatturato")    #check se il stato è cambiato in fatturato
        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #elimino attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click() #seleziono stato "Completato"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Completato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(2)

    def formato_ore_stampa(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting142-container"]').click()   #seleziono formato in sessantesimi
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting142-results"]').click()
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #sessioni di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa intervento
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        ore=self.find(By.XPATH, '//span[@style="left: 17.35%; top: 40.11%; font-size: calc(var(--scale-factor)*9.00px); font-family: sans-serif; transform: scaleX(0.996142);"]').text
        self.assertEqual(ore, "1:00")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)

        #elimina attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting142-container"]').click()   #seleziono formato in decimi
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting142-results"]').click()
        sleep(2)
    
    def visualizzare_domenica_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattiva impostazione
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[1]//th[8]')))    #check se non è visibile la domenica
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #attiva impostazione
        sleep(2)

    def vista_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting50-container"]').click()    #seleziona vista per mese
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("mese")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="fc-dayGridMonth-button fc-button fc-button-primary fc-button-active"]')))    #controlla se la vista è per mese
        sleep(1)
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting50-container"]').click()    #seleziona vista per settimana
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("settimana")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def ora_inizio_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys("01:00") #seleziono 01:00 come prima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        ora=self.find(By.XPATH, '//tr[1]//div[@class="fc-timegrid-slot-label-cushion fc-scrollgrid-shrink-cushion"]').text  #controllo se la prima ora è quella inserita
        self.assertEqual(ora, "01:00")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys("00:00") #seleziono 00:00 come prima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def ora_fine_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        ora_fine=self.find(By.XPATH, '//input[@id="setting78"]')
        ora_fine.clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys("13:30") #seleziono 13:30 come ultima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[55]//div'))) #check se non trova le ore dopo le 13.30
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        ora_fine=self.find(By.XPATH, '//input[@id="setting78"]')
        ora_fine.clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys("23:59") #seleziono 23:59 come ultima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def visualizza_informazioni_aggiuntive(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #attiva impostazione
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tr[1]//td[@class="fc-timegrid-axis fc-scrollgrid-shrink"]').text
        self.assertEqual(scritta, "Tutto il giorno")    #check se appare impostazione
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #disattiva impostazione
        sleep(2)

    def iva_predefinita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting6-container"]').click() #aggiungi iva al 10
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Aliq. Iva 10")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #aggiungi riga
        sleep(1)

        iva=self.find(By.XPATH, '//span[@id="select2-idiva-container"]').text   #check iva
        self.assertEqual(iva[2:21], "10 - Aliq. Iva 10%")
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-9"]').click() #apro Fatturazione
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting6-container"]').click() #aggiungi iva al 22
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Aliq. Iva 22")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)