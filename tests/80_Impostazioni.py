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

        # Permette inserimento sessioni degli altri tecnici (Attività)
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

        # Condizioni generali di fornitura contratti (Contratti)
        self.condizioni_generali_contratti()    #DA FINIRE

        # Crea contratto rinnocabile di default (Contratti)
        self.crea_contratto_rinnovabile()

        # Giorni di preavviso di default (Contratti)
        self.giorni_preavviso()

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

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() #apro prima fattura
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

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() #apro primo risultato
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
        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click()
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
        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click()
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
        
        #scritta=self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]').text  #non riesco a prendere il valore "Prova"
        #self.assertEqual(scritta, "Prova")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimino contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
        #torno alle impostazioni di prima
        self.find(By.XPATH, '//div[@id="impostazioni-6"]').click() #apro Contratti
        sleep(1)

        self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]').click()
        elimina=self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        elimina.clear()
        sleep(1)
        
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


