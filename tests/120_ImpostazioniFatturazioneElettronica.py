from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_fatturazione_elettronica(self):
        # Allega stampa per fattura verso Privati (1)
        self.allega_stampa_privati()

        # Allega stampa per fattura verso Aziende (2)
        self.allega_stampa_aziende()

        # Allega stampa per fattura verso PA (3)
        self.allega_stampa_PA()

        # Regime fiscale (4)
        self.regime_fiscale()

        # Tipo cassa previdenziale (5)
        self.tipo_cassa_previdenziale()

        # Causale ritenuta d'acconto (6)
        self.causale_ritenuta_acconto()

        ## TODO: Authorization ID indice PA

        ## TODO: OSMCloud services API token

        ## TODO: terzo intermediario

        # Riferimento dei documenti in fattura elettronica (10)
        self.riferimento_documenti_fattura_elettronica()

        ## TODO: OSMCloud Services API URL 

        ## TODO: OSMCloud Services API Version

        ## TODO: data inizio controlli su stati FE

        ## TODO: Movimenta magazzino da fatture di acquisto

        ## TODO: Rimuovi avviso fatture estere

        ## TODO: Creazione seriali in Import FE

        ## TODO: giorni validità fattura scartata

    def allega_stampa_privati(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click()    #attivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertEqual(allegato, "Stampa allegata")   #controllo se è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Vendite")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[1]'))
        ).click()    #disattivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotEqual(allegato, "Stampa allegata")   #controllo se non è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

    def allega_stampa_aziende(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[2]'))
        ).click()    #attivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente Estero")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertEqual(allegato, "Stampa allegata")   #controllo se è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Vendite")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[2]'))
        ).click()    #disattivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente Estero", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotEqual(allegato, "Stampa allegata")   #controllo se non è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

    def allega_stampa_PA(self):
                self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()
        #creo anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ragione_sociale_add"]'))).send_keys('Test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtipoanagrafica_add-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-tipo-container"]'))
        ).click() #seleziono tipologia di anagrafica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tipo-results"]//li[2]'))
        ).click()  #seleziono ente pubblico
        #Città
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="citta"]'))).send_keys("Prova")
        #Indirizzo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))).send_keys("via test 1")
        #C.A.P.
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="cap"]'))).send_keys("43190")
        #Codice Fiscale
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fiscale"]'))).send_keys("78954654")
        #Codice unico ufficio
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_destinatario"]'))).send_keys("CI7YID")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #salva
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[3]'))
        ).click()    #attivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Test come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Test")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertEqual(allegato, "Stampa allegata")   #controllo se è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Vendite")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[3]'))
        ).click()    #disattivo impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Test come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Test")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        allegato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-body"]//tbody//tr[1]//a'))
        ).text
        self.assertNotEqual(allegato, "Stampa allegata")   #controllo se non è stato aggiunto l'allegato
        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimino anagrafica
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Test", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')   
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]//i'))
        ).click()    #elimina ricerca

    def regime_fiscale(self):
                self.expandSidebar("Vendite")   #test con impostazioni preselezionate
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-xs btn-info"]'))
        ).click()   #visualizza fattura elettronica

        regime = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="headContent"]//span)[3]'))
        ).text   #check regime fiscale
        self.assertEqual(regime, "RF01")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click() #chiudi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting73-container"]'))
        ).click()    #cambia regime fiscale

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting73-results"]//li[2]'))
        ).click() #imposta il regime fiscale RF02

        self.expandSidebar("Vendite")   #test con impostazioni diverse
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-xs btn-info"]'))
        ).click()   #visualizza fattura elettronica

        regime = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="headContent"]//span)[3]'))
        ).text   #check regime fiscale
        self.assertEqual(regime, "RF02")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click() #chiudi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting73-container"]'))
        ).click()    #cambia regime fiscale

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting73-results"]//li[1]'))
        ).click() #imposta il regime fiscale RF01

    def tipo_cassa_previdenziale(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting74-container"]'))
        ).click()    #seleziono cassa previdenziale

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting74-results"]//li[1]'))
        ).click() #seleziono cassa TC01

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-xs btn-info"]'))
        ).click()   #visualizza fattura elettronica

        cassa = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//table[@class="tbFoglio"]//span)[1]'))
        ).text #check se è stata impostata la cassa previdenziale
        self.assertEqual(cassa, "TC01")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click() #chiudi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting74-container"]//span'))
        ).click()    #tolgo cassa previdenziale

    def causale_ritenuta_acconto(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]'))
        ).click()  #ritenuta d'acconto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_ritenuta_acconto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-calcolo_ritenuta_acconto-container"]'))
        ).click() #calcola ritenuta su imponibile

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-calcolo_ritenuta_acconto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()   #apro fattura elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        
        causale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[97]'))
        ).text #check causale
        self.assertNotEqual(causale[0], "A")    #controllo se non è stata selezionata nessuna delle causali disponibili
        self.assertNotEqual(causale[0], "B")
        self.assertNotEqual(causale[0], "C")
        self.assertNotEqual(causale[0], "D")
        self.assertNotEqual(causale[0], "E")
        self.assertNotEqual(causale[0], "F")
        self.assertNotEqual(causale[0], "G")
        self.assertNotEqual(causale[0], "I")
        self.assertNotEqual(causale[0], "L")
        self.assertNotEqual(causale[0:1], "L1")
        self.assertNotEqual(causale[0], "M")
        self.assertNotEqual(causale[0:1], "M1")
        self.assertNotEqual(causale[0:1], "M2")
        self.assertNotEqual(causale[0], "N")
        self.assertNotEqual(causale[0], "O")
        self.assertNotEqual(causale[0:1], "01")
        self.assertNotEqual(causale[0], "P")
        self.assertNotEqual(causale[0], "Q")
        self.assertNotEqual(causale[0], "R")
        self.assertNotEqual(causale[0], "S")
        self.assertNotEqual(causale[0], "T")
        self.assertNotEqual(causale[0], "U")
        self.assertNotEqual(causale[0], "V")
        self.assertNotEqual(causale[0:1], "V1")
        self.assertNotEqual(causale[0:1], "V2")
        self.assertNotEqual(causale[0], "W")
        self.assertNotEqual(causale[0], "X")
        self.assertNotEqual(causale[0], "Y")
        self.assertNotEqual(causale[0:1], "ZO")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting75-container"]'))
        ).click()    #scelgo causale A

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting75-results"]//li[1]'))
        ).click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]'))
        ).click()  #ritenuta d'acconto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_ritenuta_acconto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-calcolo_ritenuta_acconto-container"]'))
        ).click() #calcola ritenuta su imponibile

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-calcolo_ritenuta_acconto-results"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click() #cambia stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]'))
        ).click()  #seleziona stato "Emessa"

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]'))
        ).click()   #apro fattura elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        causale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[97]'))
        ).text #check causale
        self.assertEqual(causale, "A (decodiﬁca come da modello CU)")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting75-container"]//span'))
        ).click()  #togli causale

    def riferimento_documenti_fattura_elettronica(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        #aggiungi preventivo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="import_all"]'))
        ).click()    #deseleziona tutte le righe

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="checked_3"]'))
        ).click() #seleziono solo la riga del articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #stampa fattura elettronica
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[50]'))
        ).text
        self.assertEqual(riferimento[10:32], "Rif. preventivo num. 1")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()    #disattiva impostazione

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() #click su aggiungi
        self.wait_loader()
        #aggiungi preventivo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]'))
        ).click() #click su altro

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_documento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="import_all"]'))
        ).click()    #deseleziona tutte le righe

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="checked_3"]'))
        ).click() #seleziono solo la riga del articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit_btn"]'))
        ).click()   #click su aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatodocumento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #stampa fattura elettronica
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_1"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda

        riferimento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[50]'))
        ).text
        self.assertNotEqual(riferimento[10:32], "Rif. preventivo num. 1")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima

        #elimina fattura
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="impostazioni-10"]'))
        ).click() #apro Fatturazione Elettronica

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()    #attiva impostazione

